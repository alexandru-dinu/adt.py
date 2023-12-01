from dataclasses import dataclass
from typing import TypeVar

"""
data List a = Nil | Cons a List
"""

T = TypeVar("T")


class List:
    def __new__(cls, *args, **kwargs):
        if cls is List:
            raise TypeError("Class cannot be instantiated")
        return super().__new__(cls)


class Nil(List):
    pass


@dataclass
class Cons(List):
    x: T
    xs: List


if __name__ == "__main__":

    def show(lst: List):
        match lst:
            case Nil():
                return "_"
            case Cons(x, xs):
                return f"{x}:{show(xs)}"
            case _:
                assert False

    xs = Cons(1, Cons(2, Nil()))
    print(show(xs))
