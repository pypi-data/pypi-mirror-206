# -*- coding: utf-8 -*-
import json
import random
import sys
from functools import wraps
from queue import Empty
from threading import Event, Lock, Thread
from time import sleep
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    cast,
    overload,
)
from urllib.parse import ParseResult, parse_qs, urlparse
from uuid import uuid4

import dns.resolver
import grpc
from grpc import CallCredentials, Channel, ChannelConnectivity, RpcError

from esdbclient.esdbapi import (
    NODE_STATE_FOLLOWER,
    NODE_STATE_LEADER,
    NODE_STATE_REPLICA,
    BasicAuthCallCredentials,
    BatchAppendFuture,
    BatchAppendFutureQueue,
    BatchAppendRequest,
    ClusterGossipService,
    ClusterMember,
    GossipService,
    PersistentSubscriptionsService,
    StreamsService,
    SubscriptionReadRequest,
    SubscriptionReadResponse,
    handle_rpc_error,
)
from esdbclient.events import NewEvent, RecordedEvent
from esdbclient.exceptions import (
    DiscoveryFailed,
    ESDBClientException,
    FollowerNotFound,
    GossipSeedError,
    GrpcError,
    NodeIsNotLeader,
    ReadOnlyReplicaNotFound,
    StreamNotFound,
)

# Matches the 'type' of "system" events.
ESDB_SYSTEM_EVENTS_REGEX = r"\$.+"
# Matches the 'type' of "PersistentConfig" events.
ESDB_PERSISTENT_CONFIG_EVENTS_REGEX = r"PersistentConfig\d+"

DEFAULT_EXCLUDE_FILTER = (ESDB_SYSTEM_EVENTS_REGEX, ESDB_PERSISTENT_CONFIG_EVENTS_REGEX)

URI_SCHEME_ESDB = "esdb"
URI_SCHEME_ESDB_DISCOVER = "esdb+discover"

VALID_URI_SCHEMES = [
    URI_SCHEME_ESDB,
    URI_SCHEME_ESDB_DISCOVER,
]

NODE_PREFERENCE_LEADER = "leader"
NODE_PREFERENCE_FOLLOWER = "follower"
NODE_PREFERENCE_RANDOM = "random"
NODE_PREFERENCE_REPLICA = "readonlyreplica"

VALID_NODE_PREFERENCES = [
    NODE_PREFERENCE_LEADER,
    NODE_PREFERENCE_FOLLOWER,
    NODE_PREFERENCE_RANDOM,
    NODE_PREFERENCE_REPLICA,
]

_TCallable = TypeVar("_TCallable", bound=Callable[..., Any])


class ConnectionOptions:
    __slots__ = [
        "_Tls",
        "_ConnectionName",
        "_MaxDiscoverAttempts",
        "_DiscoveryInterval",
        "_GossipTimeout",
        "_NodePreference",
        "_TlsVerifyCert",
        "_DefaultDeadline",
        "_KeepAliveInterval",
        "_KeepAliveTimeout",
    ]

    def __init__(self, query: str):
        # Parse query string (case insensitivity, assume single values).
        options = {k.upper(): v[0] for k, v in parse_qs(query).items()}

        _Tls = options.get("Tls".upper())
        if _Tls is None:
            self._Tls = True
        else:
            validTlsValues = ["true", "false"]
            if _Tls not in validTlsValues:
                raise ValueError(f"'{_Tls}' not one of: {', '.join(validTlsValues)}")
            elif _Tls == "true":
                self._Tls = True
            else:
                self._Tls = False

        _ConnectionName = options.get("ConnectionName".upper())
        if _ConnectionName is None:
            self._ConnectionName = str(uuid4())
        else:
            self._ConnectionName = _ConnectionName

        _MaxDiscoverAttempts = options.get("MaxDiscoverAttempts".upper())
        if _MaxDiscoverAttempts is None:
            self._MaxDiscoverAttempts = 10
        else:
            self._MaxDiscoverAttempts = int(_MaxDiscoverAttempts)

        _DiscoveryInterval = options.get("DiscoveryInterval".upper())
        if _DiscoveryInterval is None:
            self._DiscoveryInterval = 100
        else:
            self._DiscoveryInterval = int(_DiscoveryInterval)

        _GossipTimeout = options.get("GossipTimeout".upper())
        if _GossipTimeout is None:
            self._GossipTimeout = 5
        else:
            self._GossipTimeout = int(_GossipTimeout)

        _NodePreference = options.get("NodePreference".upper())
        if _NodePreference is None:
            self._NodePreference = NODE_PREFERENCE_LEADER
        else:
            if _NodePreference not in VALID_NODE_PREFERENCES:
                raise ValueError(
                    f"'{_NodePreference}' not one of:"
                    f" {', '.join(VALID_NODE_PREFERENCES)}"
                )
            self._NodePreference = _NodePreference

        _TlsVerifyCert = options.get("TlsVerifyCert".upper())
        if _TlsVerifyCert is None:
            self._TlsVerifyCert = True
        else:
            validTlsVerifyCertValues = ["true", "false"]
            if _TlsVerifyCert not in validTlsVerifyCertValues:
                raise ValueError(
                    f"'{_TlsVerifyCert}' not one of:"
                    f" {', '.join(validTlsVerifyCertValues)}"
                )
            elif _TlsVerifyCert == "true":
                self._TlsVerifyCert = True
            else:
                self._TlsVerifyCert = False

        _DefaultDeadline = options.get("DefaultDeadline".upper())
        if _DefaultDeadline is None:
            self._DefaultDeadline: Optional[int] = None
        else:
            self._DefaultDeadline = int(_DefaultDeadline)

        _KeepAliveInterval = options.get("KeepAliveInterval".upper())
        if _KeepAliveInterval is None:
            self._KeepAliveInterval: Optional[int] = None
        else:
            self._KeepAliveInterval = int(_KeepAliveInterval)

        _KeepAliveTimeout = options.get("KeepAliveTimeout".upper())
        if _KeepAliveTimeout is None:
            self._KeepAliveTimeout: Optional[int] = None
        else:
            self._KeepAliveTimeout = int(_KeepAliveTimeout)

    @property
    def Tls(self) -> bool:
        """
        Controls whether client will use a secure channel (has to match server).

        Valid values in URI: 'true', 'false'.
        """
        return self._Tls

    @property
    def ConnectionName(self) -> str:
        """
        This value is sent as header 'connection-name' in all calls to server.

        Defaults to a new version 4 UUID string.
        """
        return self._ConnectionName

    @property
    def MaxDiscoverAttempts(self) -> int:
        """
        Number of attempts to connect to gossip before giving up.
        """
        return self._MaxDiscoverAttempts

    @property
    def DiscoveryInterval(self) -> int:
        """
        How long to wait (in milliseconds) between gossip retries.
        """
        return self._DiscoveryInterval

    @property
    def GossipTimeout(self) -> int:
        """
        How long to wait (in seconds) for a response to a request to gossip API.
        """
        return self._GossipTimeout

    @property
    def NodePreference(
        self,
    ) -> str:
        """
        Controls whether requests are directed to another node.

        Value values: 'leader', 'follower', 'random', 'readonlyreplica'.
        """
        return self._NodePreference

    @property
    def TlsVerifyCert(self) -> bool:
        """
        Controls whether certificate is verified.

        Valid values in URI: 'true', 'false'.
        """
        return self._TlsVerifyCert

    @property
    def DefaultDeadline(self) -> Optional[int]:
        """
        Default deadline (in seconds) for calls to the server that write data.
        """
        return self._DefaultDeadline

    @property
    def KeepAliveInterval(self) -> Optional[int]:
        """
        gRPC "keep alive" interval (in milliseconds).
        """
        return self._KeepAliveInterval

    @property
    def KeepAliveTimeout(self) -> Optional[int]:
        """
        gRPC "keep alive timeout" (in milliseconds).
        """
        return self._KeepAliveTimeout


class ConnectionSpec:
    __slots__ = [
        "_uri",
        "_scheme",
        "_netloc",
        "_username",
        "_password",
        "_targets",
        "_options",
    ]

    def __init__(self, uri: Optional[str] = None):
        self._uri = uri or ""
        parse_result: ParseResult = urlparse(self._uri)
        if parse_result.scheme not in VALID_URI_SCHEMES:
            raise ValueError(
                f"Invalid URI scheme: '{parse_result.scheme}' not in:"
                f" {', '.join(VALID_URI_SCHEMES)}: {uri}"
            )
        self._scheme = parse_result.scheme
        self._netloc = parse_result.netloc
        self._username = parse_result.username
        self._password = parse_result.password
        if "@" in self._netloc:
            _, _, targets = self._netloc.partition("@")
        else:
            targets = self._netloc
        self._targets = [t.strip() for t in targets.split(",") if t.strip()]
        self._options = ConnectionOptions(parse_result.query)

    @property
    def uri(self) -> str:
        return self._uri

    @property
    def scheme(self) -> str:
        return self._scheme

    @property
    def netloc(self) -> str:
        return self._netloc

    @property
    def username(self) -> Optional[str]:
        return self._username

    @property
    def password(self) -> Optional[str]:
        return self._password

    @property
    def targets(self) -> Sequence[str]:
        return self._targets

    @property
    def options(self) -> ConnectionOptions:
        return self._options


class ESDBConnection:
    def __init__(self, grpc_channel: Channel, grpc_target: str) -> None:
        self.grpc_channel = grpc_channel
        self.grpc_target = grpc_target
        self.streams = StreamsService(grpc_channel)
        self.persistent_subscriptions = PersistentSubscriptionsService(grpc_channel)
        self.gossip = GossipService(grpc_channel)
        self.cluster_gossip = ClusterGossipService(grpc_channel)
        self._channel_connectivity_state: Optional[ChannelConnectivity] = None
        self.grpc_channel.subscribe(self._receive_channel_connectivity_state)

    def _receive_channel_connectivity_state(
        self, connectivity: ChannelConnectivity
    ) -> None:
        self._channel_connectivity_state = connectivity
        # print("Channel connectivity state:", connectivity)

    def close(self) -> None:
        self.grpc_channel.unsubscribe(self._receive_channel_connectivity_state)
        self.grpc_channel.close()


def reconnect_to_leader(f: _TCallable) -> _TCallable:
    @wraps(f)
    def wrapper(self, *args, **kwargs):  # type: ignore
        assert isinstance(self, ESDBClient)
        try:
            return f(self, *args, **kwargs)

        except NodeIsNotLeader:
            if self.connection_spec.options.NodePreference == NODE_PREFERENCE_LEADER:
                self.node_is_not_leader_detected.set()
                with self.node_is_not_leader_detected_lock:
                    if self.node_is_not_leader_detected.is_set():
                        self._reconnect_to_preferred_node()
                        self.node_is_not_leader_detected.clear()
                    else:  # pragma: no cover
                        # Todo: Test with concurrent writes to wrong node state.
                        pass
                return f(self, *args, **kwargs)
            else:
                raise

    return cast(_TCallable, wrapper)


class ESDBClient:
    """
    Encapsulates the EventStoreDB gRPC API.
    """

    def __init__(
        self,
        uri: Optional[str] = None,
        *,
        root_certificates: Optional[str] = None,
    ) -> None:
        self.node_is_not_leader_detected = Event()
        self.node_is_not_leader_detected_lock = Lock()
        self.root_certificates = root_certificates
        self.connection_spec = ConnectionSpec(uri)

        self._default_deadline = self.connection_spec.options.DefaultDeadline

        self.grpc_options: Dict[str, Any] = {
            "grpc.max_receive_message_length": 17 * 1024 * 1024,
        }
        if self.connection_spec.options.KeepAliveInterval is not None:
            self.grpc_options["grpc.keepalive_ms"] = (
                self.connection_spec.options.KeepAliveInterval
            )
        if self.connection_spec.options.KeepAliveTimeout is not None:
            self.grpc_options["grpc.keepalive_timeout_ms"] = (
                self.connection_spec.options.KeepAliveTimeout
            )

        self._call_metadata = (
            ("connection-name", self.connection_spec.options.ConnectionName),
        )

        if self.connection_spec.options.Tls:
            self._call_credentials = self._construct_call_credentials(
                self.connection_spec.username, self.connection_spec.password
            )
        else:
            self._call_credentials = None

        self._connection = self._connect_to_preferred_node()

        self._batch_append_futures_lock = Lock()
        self._batch_append_futures_queue = BatchAppendFutureQueue()
        self._batch_append_thread = Thread(
            target=self._batch_append_future_result_loop, daemon=True
        )
        self._batch_append_thread.start()

    def _construct_call_credentials(
        self, username: Optional[str], password: Optional[str]
    ) -> Optional[CallCredentials]:
        if username and password:
            return grpc.metadata_call_credentials(
                BasicAuthCallCredentials(username, password)
            )
        else:
            return None

    def _connect_to_preferred_node(self) -> ESDBConnection:
        # Obtain the gossip seed (a list of gRPC targets).
        if self.connection_spec.scheme == URI_SCHEME_ESDB_DISCOVER:
            assert len(self.connection_spec.targets) == 1
            cluster_fqdn = self.connection_spec.targets[0]
            answers = dns.resolver.resolve(cluster_fqdn, "A")
            gossip_seed: Sequence[str] = [f"{s.address}:2113" for s in answers]

        else:
            gossip_seed = self.connection_spec.targets

        # Check the gossip seed isn't empty.
        if len(gossip_seed) == 0:
            raise GossipSeedError(self.connection_spec.uri)

        # Iterate through the gossip seed...
        attempts = 0
        connection: Optional[ESDBConnection] = None
        cluster_members: Sequence[ClusterMember] = []
        while (
            len(cluster_members) == 0
            and attempts < self.connection_spec.options.MaxDiscoverAttempts
        ):
            for grpc_target in gossip_seed:
                attempts += 1
                # Construct a connection.
                connection = self._construct_connection(grpc_target)

                # Read the gossip (get cluster members).
                try:
                    cluster_members = connection.gossip.read(
                        timeout=self.connection_spec.options.GossipTimeout,
                        metadata=self._call_metadata,
                        credentials=self._call_credentials,
                    )
                except GrpcError:
                    sleep(self.connection_spec.options.DiscoveryInterval / 1000)
                else:
                    break
                connection.close()

        if len(cluster_members) == 0 or connection is None:
            raise DiscoveryFailed(gossip_seed)

        # Select a member according to node preference.
        # Todo: What about if leader election is happening, and states aren't settled?
        node_preference = self.connection_spec.options.NodePreference
        cluster_member: ClusterMember
        if node_preference == NODE_PREFERENCE_LEADER:
            leaders = [c for c in cluster_members if c.state == NODE_STATE_LEADER]
            assert len(leaders) == 1, f"Expected one leader, discovered {len(leaders)}"
            cluster_member = leaders[0]
        elif node_preference == NODE_PREFERENCE_FOLLOWER:
            followers = [c for c in cluster_members if c.state == NODE_STATE_FOLLOWER]
            if len(followers) == 0:
                raise FollowerNotFound()
            cluster_member = random.choice(followers)
        elif node_preference == NODE_PREFERENCE_REPLICA:
            replicas = [c for c in cluster_members if c.state == NODE_STATE_REPLICA]
            if len(replicas) == 0:
                raise ReadOnlyReplicaNotFound()
            # Todo: Somehow cover this with a test (how to setup a read-only replica?)
            cluster_member = random.choice(replicas)  # pragma: no cover
        else:
            assert node_preference == NODE_PREFERENCE_RANDOM
            cluster_member = random.choice(cluster_members)

        # Maybe reconnect to selected cluster member.
        if len(cluster_members) > 1:  # forgive not "advertising" single node
            # Check gossip seed target matches advertised member address and port.
            grpc_target = f"{cluster_member.address}:{cluster_member.port}"
            if connection.grpc_target != grpc_target:
                # Need to connect to a different node.
                connection.close()
                connection = self._construct_connection(grpc_target)

        return connection

    def _reconnect_to_preferred_node(self) -> None:
        new_c = self._connect_to_preferred_node()
        old_c, self._connection = self._connection, new_c
        old_c.close()

    def _construct_connection(self, grpc_target: str) -> ESDBConnection:
        grpc_options: Tuple[Tuple[str, str], ...] = tuple(self.grpc_options.items())
        if self.connection_spec.options.Tls is True:
            if self.root_certificates is None:
                raise ValueError("root_certificates is required for secure connection")

            assert self.connection_spec.username
            assert self.connection_spec.password
            channel_credentials = grpc.ssl_channel_credentials(
                root_certificates=self.root_certificates.encode()
            )
            grpc_channel = grpc.secure_channel(
                target=grpc_target,
                credentials=channel_credentials,
                options=grpc_options,
            )
        else:
            grpc_channel = grpc.insecure_channel(
                target=grpc_target, options=grpc_options
            )

        return ESDBConnection(grpc_channel=grpc_channel, grpc_target=grpc_target)

    def _batch_append_future_result_loop(self) -> None:
        # while self._channel_connectivity_state is not ChannelConnectivity.SHUTDOWN:
        try:
            self._connection.streams.batch_append_multiplexed(
                futures_queue=self._batch_append_futures_queue,
                timeout=None,
                metadata=self._call_metadata,
                credentials=self._call_credentials,
            )
        except ESDBClientException as e:
            self._clear_batch_append_futures_queue(e)
        else:
            self._clear_batch_append_futures_queue(  # pragma: no cover
                ESDBClientException("Request not sent")
            )
        # print("Looping on call to batch_append_multiplexed()....")

    def _clear_batch_append_futures_queue(self, error: ESDBClientException) -> None:
        with self._batch_append_futures_lock:
            try:
                while True:
                    future = self._batch_append_futures_queue.get(block=False)
                    future.set_exception(error)  # pragma: no cover
            except Empty:
                pass

    def append_events_multiplexed(
        self,
        stream_name: str,
        expected_position: Optional[int],
        events: Iterable[NewEvent],
        timeout: Optional[float] = None,
    ) -> int:
        timeout = timeout if timeout is not None else self._default_deadline
        batch_append_request = BatchAppendRequest(
            stream_name=stream_name, expected_position=expected_position, events=events
        )
        future = BatchAppendFuture(batch_append_request=batch_append_request)
        with self._batch_append_futures_lock:
            self._batch_append_futures_queue.put(future)
        response = future.result(timeout=timeout)
        assert isinstance(response.commit_position, int)
        return response.commit_position

    @reconnect_to_leader
    def append_events(
        self,
        stream_name: str,
        expected_position: Optional[int],
        events: Iterable[NewEvent],
        timeout: Optional[float] = None,
    ) -> int:
        timeout = timeout if timeout is not None else self._default_deadline
        return self._connection.streams.batch_append(
            BatchAppendRequest(
                stream_name=stream_name,
                expected_position=expected_position,
                events=events,
            ),
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        ).commit_position

    @reconnect_to_leader
    def append_event(
        self,
        stream_name: str,
        expected_position: Optional[int],
        event: NewEvent,
        timeout: Optional[float] = None,
    ) -> int:
        """
        Appends a new event to the named stream.
        """
        timeout = timeout if timeout is not None else self._default_deadline
        return self._connection.streams.append(
            stream_name=stream_name,
            expected_position=expected_position,
            events=[event],
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    @reconnect_to_leader
    def delete_stream(
        self,
        stream_name: str,
        expected_position: Optional[int],
        timeout: Optional[float] = None,
    ) -> None:
        timeout = timeout if timeout is not None else self._default_deadline
        self._connection.streams.delete(
            stream_name=stream_name,
            expected_position=expected_position,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    @reconnect_to_leader
    def tombstone_stream(
        self,
        stream_name: str,
        expected_position: Optional[int],
        timeout: Optional[float] = None,
    ) -> None:
        timeout = timeout if timeout is not None else self._default_deadline
        self._connection.streams.tombstone(
            stream_name=stream_name,
            expected_position=expected_position,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def read_stream_events(
        self,
        stream_name: str,
        stream_position: Optional[int] = None,
        backwards: bool = False,
        limit: int = sys.maxsize,
        timeout: Optional[float] = None,
    ) -> Iterable[RecordedEvent]:
        """
        Reads recorded events from the named stream.
        """
        return self._connection.streams.read(
            stream_name=stream_name,
            stream_position=stream_position,
            backwards=backwards,
            limit=limit,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def read_all_events(
        self,
        commit_position: Optional[int] = None,
        backwards: bool = False,
        filter_exclude: Sequence[str] = DEFAULT_EXCLUDE_FILTER,
        filter_include: Sequence[str] = (),
        limit: int = sys.maxsize,
        timeout: Optional[float] = None,
    ) -> Iterable[RecordedEvent]:
        """
        Reads recorded events in "all streams" in the database.
        """
        return self._connection.streams.read(
            commit_position=commit_position,
            backwards=backwards,
            filter_exclude=filter_exclude,
            filter_include=filter_include,
            limit=limit,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def get_stream_position(
        self,
        stream_name: str,
        timeout: Optional[float] = None,
    ) -> Optional[int]:
        """
        Returns the current position of the end of a stream.
        """
        try:
            last_event = list(
                self._connection.streams.read(
                    stream_name=stream_name,
                    backwards=True,
                    limit=1,
                    timeout=timeout,
                    metadata=self._call_metadata,
                    credentials=self._call_credentials,
                )
            )[0]
        except StreamNotFound:
            return None
        else:
            return last_event.stream_position

    def get_commit_position(
        self,
        timeout: Optional[float] = None,
        filter_exclude: Sequence[str] = DEFAULT_EXCLUDE_FILTER,
    ) -> int:
        """
        Returns the current commit position of the database.
        """
        recorded_events = self.read_all_events(
            backwards=True,
            filter_exclude=filter_exclude,
            limit=1,
            timeout=timeout,
        )
        commit_position = 0
        for ev in recorded_events:
            assert ev.commit_position is not None
            commit_position = ev.commit_position
        return commit_position

    def get_stream_metadata(
        self, stream_name: str, timeout: Optional[float] = None
    ) -> Tuple[Dict[str, Any], Optional[int]]:
        """
        Gets the stream metadata.
        """
        metadata_stream_name = f"$${stream_name}"
        try:
            metadata_events = list(
                self.read_stream_events(
                    stream_name=metadata_stream_name,
                    backwards=True,
                    limit=1,
                    timeout=timeout,
                )
            )
        except StreamNotFound:
            return {}, None
        else:
            metadata_event = metadata_events[0]
            return json.loads(metadata_event.data), metadata_event.stream_position

    @reconnect_to_leader
    def set_stream_metadata(
        self,
        stream_name: str,
        metadata: Dict[str, Any],
        expected_position: Optional[int] = -1,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Sets the stream metadata.
        """
        timeout = timeout if timeout is not None else self._default_deadline

        metadata_stream_name = f"$${stream_name}"
        metadata_event = NewEvent(
            type="$metadata",
            data=json.dumps(metadata).encode("utf8"),
        )
        self.append_event(
            stream_name=metadata_stream_name,
            expected_position=expected_position,
            event=metadata_event,
            timeout=timeout,
        )

    def subscribe_all_events(
        self,
        commit_position: Optional[int] = None,
        filter_exclude: Sequence[str] = DEFAULT_EXCLUDE_FILTER,
        filter_include: Sequence[str] = (),
        timeout: Optional[float] = None,
    ) -> Iterator[RecordedEvent]:
        """
        Starts a catch-up subscription, from which all
        recorded events in the database can be received.
        """
        read_resp = self._connection.streams.read(
            commit_position=commit_position,
            filter_exclude=filter_exclude,
            filter_include=filter_include,
            subscribe=True,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )
        return CatchupSubscription(read_resp=read_resp)

    def subscribe_stream_events(
        self,
        stream_name: str,
        stream_position: Optional[int] = None,
        timeout: Optional[float] = None,
    ) -> Iterator[RecordedEvent]:
        """
        Starts a catch-up subscription from which
        recorded events in a stream can be received.
        """
        read_resp = self._connection.streams.read(
            stream_name=stream_name,
            stream_position=stream_position,
            subscribe=True,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )
        return CatchupSubscription(read_resp=read_resp)

    @overload
    def create_subscription(
        self,
        group_name: str,
        *,
        filter_exclude: Sequence[str] = DEFAULT_EXCLUDE_FILTER,
        filter_include: Sequence[str] = (),
        timeout: Optional[float] = None,
    ) -> None:
        """
        Signature for creating persistent subscription from start of database.
        """

    @overload
    def create_subscription(
        self,
        group_name: str,
        *,
        commit_position: int,
        filter_exclude: Sequence[str] = DEFAULT_EXCLUDE_FILTER,
        filter_include: Sequence[str] = (),
        timeout: Optional[float] = None,
    ) -> None:
        """
        Signature for creating persistent subscription from a commit position.
        """

    @overload
    def create_subscription(
        self,
        group_name: str,
        *,
        from_end: bool = True,
        filter_exclude: Sequence[str] = DEFAULT_EXCLUDE_FILTER,
        filter_include: Sequence[str] = (),
        timeout: Optional[float] = None,
    ) -> None:
        """
        Signature for creating persistent subscription from end of database.
        """

    @reconnect_to_leader
    def create_subscription(
        self,
        group_name: str,
        from_end: bool = False,
        commit_position: Optional[int] = None,
        filter_exclude: Sequence[str] = DEFAULT_EXCLUDE_FILTER,
        filter_include: Sequence[str] = (),
        timeout: Optional[float] = None,
    ) -> None:
        """
        Creates a persistent subscription on all streams.
        """
        timeout = timeout if timeout is not None else self._default_deadline

        self._connection.persistent_subscriptions.create(
            group_name=group_name,
            from_end=from_end,
            commit_position=commit_position,
            filter_exclude=filter_exclude,
            filter_include=filter_include,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    @overload
    def create_stream_subscription(
        self,
        group_name: str,
        stream_name: str,
        *,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Signature for creating stream subscription from start of stream.
        """

    @overload
    def create_stream_subscription(
        self,
        group_name: str,
        stream_name: str,
        *,
        stream_position: int,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Signature for creating stream subscription from stream position.
        """

    @overload
    def create_stream_subscription(
        self,
        group_name: str,
        stream_name: str,
        *,
        from_end: bool = True,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Signature for creating stream subscription from end of stream.
        """

    @reconnect_to_leader
    def create_stream_subscription(
        self,
        group_name: str,
        stream_name: str,
        from_end: bool = False,
        stream_position: Optional[int] = None,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Creates a persistent subscription on one stream.
        """
        timeout = timeout if timeout is not None else self._default_deadline

        self._connection.persistent_subscriptions.create(
            group_name=group_name,
            stream_name=stream_name,
            from_end=from_end,
            stream_position=stream_position,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def read_subscription(
        self, group_name: str, timeout: Optional[float] = None
    ) -> Tuple[SubscriptionReadRequest, SubscriptionReadResponse]:
        """
        Reads a persistent subscription on all streams.
        """
        return self._connection.persistent_subscriptions.read(
            group_name=group_name,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def read_stream_subscription(
        self, group_name: str, stream_name: str, timeout: Optional[float] = None
    ) -> Tuple[SubscriptionReadRequest, SubscriptionReadResponse]:
        """
        Reads a persistent subscription on one stream.
        """
        return self._connection.persistent_subscriptions.read(
            group_name=group_name,
            stream_name=stream_name,
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def read_gossip(self, timeout: Optional[float] = None) -> Sequence[ClusterMember]:
        timeout = (
            timeout
            if timeout is not None
            else self.connection_spec.options.GossipTimeout
        )
        return self._connection.gossip.read(
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def read_cluster_gossip(
        self, timeout: Optional[float] = None
    ) -> Sequence[ClusterMember]:
        timeout = (
            timeout
            if timeout is not None
            else self.connection_spec.options.GossipTimeout
        )
        return self._connection.cluster_gossip.read(
            timeout=timeout,
            metadata=self._call_metadata,
            credentials=self._call_credentials,
        )

    def close(self) -> None:
        """
        Closes the gRPC channel.
        """
        try:
            c = self._connection
        except AttributeError:
            pass
        else:
            c.close()

    def __del__(self) -> None:
        self.close()


class CatchupSubscription(Iterator[RecordedEvent]):
    """
    Encapsulates read response for a catch-up subscription.
    """

    def __init__(
        self,
        read_resp: Iterable[RecordedEvent],
    ):
        self.read_resp = iter(read_resp)

    def __iter__(self) -> Iterator[RecordedEvent]:
        return self

    def __next__(self) -> RecordedEvent:
        try:
            return next(self.read_resp)
        except RpcError as e:
            raise handle_rpc_error(e) from e  # pragma: no cover
