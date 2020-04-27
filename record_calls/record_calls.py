from typing import List, Dict
from functools import wraps
from dataclasses import dataclass


# # Base
# def record_calls(func):
#     """Records the number of times func is called."""
#     def wrapper(*args, **kwargs):
#         func.call_count += 1
#         return func(*args, **kwargs)

#     func.call_count = 0
#     return wrapper

# @record_calls
# def greet(name="world"):
#     """Greet someone by their name.

#     >>> greet("Atty")
#     Hello Atty
#     >>> greet.call_count
#     1
#     >>> greet()
#     Hello world
#     >>> greet.call_count
#     2
#     """
#     print(f"Hello {name}")


# # Bonus 1
# def record_calls(func):
#     """Records the number of times func is called. Keeps func metadata."""
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         return func(*args, **kwargs)

#     wrapper.call_count = 0
#     return wrapper

# @record_calls
# def greet(name="world"):
#     """Greet someone by their name."""
#     print(f"Hello {name}")


# # Bonus 2
# @dataclass
# class Call:
#     args: List
#     kwargs: Dict

# def record_calls(func):
#     """Records the number of times func is called."""
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         wrapper.calls.append(Call(args=args, kwargs=kwargs))
#         return func(*args, **kwargs)

#     wrapper.call_count = 0
#     wrapper.calls = []
#     return wrapper


# @record_calls
# def greet(name="world"):
#     """Greet someone by their name.

#     >>> greet("Atty")
#     Hello Atty
#     >>> greet.calls[0].args
#     ('Atty',)
#     >>> greet.calls[0].kwargs
#     {}
#     >>> greet(name="Atty")
#     Hello Atty
#     >>> greet.calls[1].args
#     ()
#     >>> greet.calls[1].kwargs
#     {'name': 'Atty'}
#     """
#     print(f"Hello {name}")


# Bonus 3
@dataclass
class Call:
    args: List
    kwargs: Dict
    return_value: int
    exception: Exception

NO_RETURN = object()

def record_calls(func):
    """Records the number of times func is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        try:
            return_value = func(*args, **kwargs)
            wrapper.calls.append(Call(args=args, kwargs=kwargs,
                                      return_value=return_value, exception=None))
        except Exception as e:
            wrapper.calls.append(Call(args=args, kwargs=kwargs,
                                      return_value=NO_RETURN, exception=e))
        return func(*args, **kwargs)

    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper

@record_calls
def cube(n):
    """
    >>> cube(3)
    27
    >>> cube.calls
    [Call(args=(3,), kwargs={}, return_value=27, exception=None)]
    >>> cube(None)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
    >>> cube.calls[-1].exception
    TypeError("unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'")
    >>> cube.calls[-1].return_value == NO_RETURN
    True
    """
    return n**3