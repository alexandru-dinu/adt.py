"""
Input: Haskell-like ADT definition
```
data List Any = Null | Cons Any (List Any)

Output: Python code
```
class List:
    Nil: []
    Cons: [("x", Any), ("xs", "List")]
```
"""

from dataclasses import dataclass
from typing import Any  # noqa

import lark

from adt.lib import ADT  # noqa

ADT_GRAMMAR = """ 
    start: "data" kind kind_sub_type* "=" cons_list

    kind: CNAME
    kind_sub_type: typing
    
    cons_list: cons ("|" cons)*
    cons: CNAME cons_sub_type*
    cons_sub_type: typing | "(" cons ")"

    typing: CNAME 

    %import common.CNAME
    %import common.WS
    %ignore WS
"""


@dataclass
class ADTStructure:
    kind: str
    kind_sub_types: list[str]
    cons_list: list[dict]


class ADTTransformer(lark.Transformer):
    def start(self, items):
        kind, *kind_sub_types, cons_list = items
        return {
            "kind": kind,
            "kind_sub_types": sum(kind_sub_types, []),
            "cons_list": cons_list,
        }

    def kind(self, token):
        return token[0].value

    def kind_sub_type(self, items):
        return items

    def cons(self, items):
        cons_name, *cons_sub_types = items
        return {"cons_name": cons_name.value, "cons_sub_types": cons_sub_types}

    def cons_list(self, items):
        return items

    def cons_sub_type(self, items):
        return items[0]

    def typing(self, token):
        return token[0].value


def parse_adt(adt: str) -> ADTStructure:
    parser = lark.Lark(
        ADT_GRAMMAR, start="start", parser="lalr", transformer=ADTTransformer()
    )

    return parser.parse(adt)


if __name__ == "__main__":
    t = parse_adt("data Color = A | B | C")
    print(t)
