
import collections.abc
import inspect
import typing
from typing import (
    Any,
    Callable,
    Iterable,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
    get_type_hints,
)

# An ArgumentMapper converts a query+agent ID into a supported func argument (e.g. "query" or "user_storage")
ArgumentMapper = Callable[[api.AgentQuery, str], Any]

# BoundArgumentMapper is an ArgumentMapper that has been bound to a named parameter.
BoundArgumentMapper = Tuple[str, ArgumentMapper]

class AgentFunc:
    """A Python function that can be invoked by aido.

    Wrapped functions can take up to three arguments:

    1. A message or query of type: `str`, `api.AgentMessage`, or `api.AgentQuery`;
       name: "query", or "message"; or the first parameter if no other rules apply.
    2. A user storage object of type `user_storage.UserStorage` or name "user_storage".
    3. An OAuth handler of type `oauth.OAuthHandler` or name "oauth_handler".

    The semantics of each parameter are inferred by type annotation or name/position if no
    type annotations are present.
    """

    def __init__(
        self,
        impl: Callable,
        argument_mappers: Iterable[BoundArgumentMapper],
        allow_multiple_responses: bool,
    ):
        self._impl = impl
        self._argument_mappers = tuple(argument_mappers)
        self._allow_multiple_responses = allow_multiple_responses