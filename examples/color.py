"""
data Color = Red | Green | Blue
"""


# base type (type constructor): cannot be instantiated
class Color:
    def __new__(cls, *args, **kwargs):
        if cls is Color:
            raise TypeError("Class cannot be instantiated")
        return object.__new__(cls, *args, **kwargs)


# Red, Green, Blue: data constructors


@dataclass
class Red(Color):
    pass


@dataclass
class Green(Color):
    pass


@dataclass
class Blue(Color):
    pass
