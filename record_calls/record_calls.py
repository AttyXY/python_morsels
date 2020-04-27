from typing import List, Dict


# Base
def record_calls(func):
    """Records the number of times func is called."""
    def wrapper(*args, **kwargs):
        func.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
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
