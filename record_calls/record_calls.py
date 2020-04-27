from typing import List, Dict
from functools import wraps
from dataclasses import dataclass


# Base
def record_calls(func):
    """Records the number of times func is called."""
    def wrapper(*args, **kwargs):
        func.call_count += 1
        return func(*args, **kwargs)

    func.call_count = 0
    return wrapper

@record_calls
def greet(name="world"):
    """Greet someone by their name.

    >>> greet("Atty")
    Hello Atty
    >>> greet.call_count
    1
    >>> greet()
    Hello world
    >>> greet.call_count
    2
    """
    print(f"Hello {name}")


# Bonus 1
def record_calls(func):
    """Records the number of times func is called. Keeps func metadata."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper

@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")


# Bonus 2
@dataclass
class Call:
    args: List
    kwargs: Dict

def record_calls(func):
    """Records the number of times func is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args=args, kwargs=kwargs))
        return func(*args, **kwargs)

    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper


@record_calls
def greet(name="world"):
    """Greet someone by their name.

    >>> greet("Atty")
    Hello Atty
    >>> greet.calls[0].args
    ('Atty',)
    >>> greet.calls[0].kwargs
    {}
    >>> greet(name="Atty")
    Hello Atty
    >>> greet.calls[1].args
    ()
    >>> greet.calls[1].kwargs
    {'name': 'Atty'}
    """
    print(f"Hello {name}")
