from contextlib import contextmanager
from typing import Tuple, Optional
from types import TracebackType
from dataclasses import dataclass


# Base
@contextmanager
def suppress(to_suppress: Exception) -> None:
    """
    >>> with suppress(NameError):
    ...     print("Hi!")
    ...     print("It's nice to meet you,", name)
    ...     print("Goodbye!")
    ...
    Hi!
    >>> with suppress(TypeError):
    ...     print("Hi!")
    ...     print("It's nice to meet you,", name)
    ...     print("Goodbye!")
    ...
    Hi!
    Traceback (most recent call last):
    ...
    NameError: name 'name' is not defined
    >>> x = 0
    >>> with suppress(ValueError):
    ...     x = int('hello')
    ...
    >>> x
    0
    """
    try:
        yield
    except to_suppress:
        pass # catch and ignore all exceptions


# Bonus 1
@contextmanager
def suppress(*to_suppress: Tuple[Exception]) -> None:
    """
    >>> with suppress(ValueError, TypeError):
    ...     x = int('hello')
    ...
    >>> with suppress(ValueError, TypeError):
    ...     x = int(None)
    ...
    """
    try:
        yield
    except to_suppress:
        pass # catch and ignore all exceptions


# Bonus 2
@dataclass
class ExceptionInfo:
    exception: Optional[Exception] = None
    traceback: Optional[TracebackType] = None

@contextmanager
def suppress(*to_suppress: Tuple[Exception]) -> None:
    """
    >>> with suppress(ValueError, TypeError) as context:
    ...     x = int('hello')
    ...
    >>> context.exception
    ValueError("invalid literal for int() with base 10: 'hello'")
    >>> context.traceback   #doctest: +ELLIPSIS
    <traceback object at 0x...>
    """
    info = ExceptionInfo()
    try:
        yield info
    except to_suppress as e:
        info.exception = e
        info.traceback = e.__traceback__


# Bonus 3
@dataclass
class ExceptionInfo:
    exception: Optional[Exception] = None
    traceback: Optional[TracebackType] = None

@contextmanager
def suppress(*to_suppress: Tuple[Exception]) -> None:
    """
    >>> @suppress(TypeError)
    ... def len_or_none(thing):
    ...     return len(thing)
    ...
    >>> len_or_none('hello')
    5
    >>> len_or_none(64)
    >>> len_or_none([2, 4, 8])
    3
    >>> len_or_none()
    >>> len_or_none([])
    0
    """
    info = ExceptionInfo()
    try:
        yield info
    except to_suppress as e:
        info.exception = e
        info.traceback = e.__traceback__