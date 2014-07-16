# -*- coding: utf-8 -*-
"""Contains exceptions and error codes."""


class CodeMessageException(Exception):
    """An exception with code and message attributes."""

    def __init__(self, code, msg):
        super(CodeMessageException, self).__init__()
        self.code = code
        self.msg = msg


class SynapseError(CodeMessageException):
    """A base error which can be caught for all synapse events."""
    pass


class RoomError(SynapseError):
    """An error raised when a room event fails."""
    pass


class RegistrationError(SynapseError):
    """An error raised when a registration event fails."""
    pass


def cs_error(msg, code=0, **kwargs):
    """ Utility method for constructing an error response for client-server
    interactions.

    Args:
        msg : The error message.
        code : The error code.
        kwargs : Additional keys to add to the response.
    Returns:
        A dict representing the error response JSON.
    """
    err = {"error": msg, "errcode": code}
    for key, value in kwargs.iteritems():
        err[key] = value
    return err