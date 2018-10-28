from typing import Callable, Dict


Key = Dict[object, Callable]
Types = Dict[object, Callable]


def compare_dicts(a: Dict, b: Dict, keys: Key = {}, types: Types = {}) -> bool:

    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        for dict_to_comp in a, b:
            for key_to_ignore in keys:
                if key_to_ignore in dict_to_comp:
                    del dict_to_comp[key_to_ignore]
        if not sorted(a.keys()) == sorted(b.keys()):
            return False
        return all(
            [compare_dicts(a[key], b[key], keys, types)
             for key in a.keys() if key not in keys]
        )

    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(
            [compare_dicts(a_element, b_element, keys, types)
             for a_element, b_element in zip(a, b)]
        )

    if type(a) in types:
        return types[type(a)](a, b)
    return a == b
