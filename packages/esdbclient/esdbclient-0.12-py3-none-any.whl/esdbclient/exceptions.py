# -*- coding: utf-8 -*-
class ESDBClientException(Exception):
    """
    Base class for exceptions raised by the client.
    """


class GrpcError(ESDBClientException):
    """
    Base class for exceptions raised by gRPC.
    """


class ServiceUnavailable(GrpcError):
    """
    Raised when gRPC service is unavailable.
    """


class DeadlineExceeded(GrpcError):
    """
    Raised when gRPC operation times out.
    """


class NodeIsNotLeader(GrpcError):
    """
    Raised when client attempts to write to a node that is not a leader.
    """


class FollowerNotFound(ESDBClientException):
    """
    Raised when NodePreference is 'follower' but the cluster has no such nodes.
    """


class ReadOnlyReplicaNotFound(ESDBClientException):
    """
    Raised when NodePreference is 'readonlyreplica' but the cluster has no such nodes.
    """


class StreamNotFound(ESDBClientException):
    """
    Raised when EventStoreDB stream is not found.
    """


class ExpectedPositionError(ESDBClientException):
    """
    Raised when expected position does not match the
    actual position of the last event in a stream.
    """


class AccessDeniedError(ESDBClientException):
    """
    Raised when access is denied by the server.
    """


class StreamDeletedError(ESDBClientException):
    """
    Raised when appending to a deleted stream.
    """


class TimeoutError(ESDBClientException):
    """
    Raised when append operation is timed out by the server.
    """


class UnknownError(ESDBClientException):
    """
    Raised when append operation fails with an "unknown" error.
    """


class InvalidTransactionError(ESDBClientException):
    """
    Raised when append operation fails with an "invalid transaction" error.
    """


class MaximumAppendSizeExceededError(ESDBClientException):
    """
    Raised when append operation fails with a "maximum append size exceeded" error.
    """


class BadRequestError(ESDBClientException):
    """
    Raised when append operation fails with a "bad request" error.
    """


class GossipSeedError(ESDBClientException):
    """
    Raised when client has no gossip seeds.
    """


class DiscoveryFailed(ESDBClientException):
    """
    Raised when client fails to satisfy node preference using gossip cluster info.
    """
