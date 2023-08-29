from dataclasses import make_dataclass
from typing import Any, Callable


class ADTMeta(type):
    def __new__(cls, name, bases, clsdict):
        base = make_dataclass(name, fields=[], bases=(object,))

        for data_cons, fields in clsdict["__annotations__"].items():
            globals().update(
                {data_cons: make_dataclass(data_cons, fields, bases=(base,))}
            )

        return base


def ADT(namespace: dict[str, Any]) -> Callable[[type], type]:
    def wraps(cls: type) -> type:
        base = make_dataclass(cls.__name__, fields=[], bases=(object,))

        for data_cons, fields in cls.__dict__["__annotations__"].items():
            namespace.update(
                {data_cons: make_dataclass(data_cons, fields, bases=(base,))}
            )

        return base

    return wraps


def impl_for(cls):
    def wrap(func):
        setattr(cls, func.__name__, func)
        for subcls in cls.__subclasses__():
            setattr(subcls, func.__name__, func)

        # TODO: have to mangle name so that func(...) is no longer available, only x.func(...)
        return func

    return wrap


if __name__ == "__main__":

    class List(metaclass=ADTMeta):
        """
        data List a = Null | Cons a (List a)
        """

        Nil: []
        Cons: [("x", Any), ("xs", "List")]

    @ADT(namespace=globals())
    class Tree:
        """
        data Tree a = Null | Leaf a | Node a [Tree a]
        """

        Null: []
        Leaf: [("val", Any)]
        Node: [("val", Any), ("children", list["Tree"])]

    @impl_for(List)
    def show(self) -> str:
        match self:
            case Nil():
                return "<END>"
            case Cons(head, tail):
                return f"{head}:{tail.show()}"

    @impl_for(Tree)
    def show(self, depth=0) -> str:
        match self:
            case Null():
                return ""
            case Leaf(x):
                return f"{x}|{depth}"
            case Node(x, xs):
                rest = ":".join([r.show(depth + 1) for r in xs])
                return f"({x}|{depth}):{rest}"

    lst = Cons(1, Cons(2, Cons(3, Nil())))
    assert lst.show() == "1:2:3:<END>"

    tree = Node(val=1, children=[Leaf(2), Leaf(3), Leaf(4)])
    assert tree.show() == "(1|0):2|1:3|1:4|1"
