import pytest

from adt.compiler import parse_adt

test_cases = [
    (
        "data Color = Red | Green | Blue",
        {
            "kind": "Color",
            "kind_sub_types": [],
            "cons_list": [
                {"cons_name": "Red", "cons_sub_types": []},
                {"cons_name": "Green", "cons_sub_types": []},
                {"cons_name": "Blue", "cons_sub_types": []},
            ],
        },
    ),
    (
        "data Either a b = Left a | Right b",
        {
            "kind": "Either",
            "kind_sub_types": ["a", "b"],
            "cons_list": [
                {"cons_name": "Left", "cons_sub_types": ["a"]},
                {"cons_name": "Right", "cons_sub_types": ["b"]},
            ],
        },
    ),
    (
        "data List a = Null | Cons a (List a)",
        {
            "kind": "List",
            "kind_sub_types": ["a"],
            "cons_list": [
                {"cons_name": "Null", "cons_sub_types": []},
                {
                    "cons_name": "Cons",
                    "cons_sub_types": [ # TODO: fix mix of simple vs composite sub-types
                        "a",
                        {"cons_name": "List", "cons_sub_types": ["a"]},
                    ],
                },
            ],
        },
    ),
    (
        "data BTree a = Null | Leaf a | Node a (BTree a) (BTree a)",
        {
            "kind": "BTree",
            "kind_sub_types": ["a"],
            "cons_list": [
                {"cons_name": "Null", "cons_sub_types": []},
                {
                    "cons_name": "Leaf",
                    "cons_sub_types": ["a"],
                },
                {
                    "cons_name": "Node",
                    "cons_sub_types": [
                        "a",
                        {"cons_name": "BTree", "cons_sub_types": ["a"]},
                        {"cons_name": "BTree", "cons_sub_types": ["a"]},
                    ],
                },
            ],
        },
    ),
]


@pytest.mark.parametrize("adt, parsed", test_cases)
def test_parser(adt: str, parsed: dict):
    res = parse_adt(adt)
    assert res == parsed, f"For {adt=}, expected: {parsed}, but got: {res}"
