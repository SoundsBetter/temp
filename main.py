import typing as t
from functools import wraps

from temp.my_types import P, T


def my_decorator(func: t.Callable[P, T]) -> t.Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> t.Callable[P, T]:
        print("I'm decorator")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def foo() -> None:
    print("I'm foo")


foo()
