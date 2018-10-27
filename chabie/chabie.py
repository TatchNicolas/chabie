from typing import Dict, List, Tuple, Callable


Key = List[Tuple[type, Callable]]
Ignore = List[str]


def compare_dicts(a: Dict, b: Dict,
                  cmps: Key = [], ignore: Ignore = []) -> bool:

    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        for dict_to_comp in a, b:
            for key_to_ignore in ignore:
                if key_to_ignore in dict_to_comp:
                    del dict_to_comp[key_to_ignore]
        if not sorted(a.keys()) == sorted(b.keys()):
            return False
        return all(
            [compare_dicts(a[key], b[key], cmps, ignore)
             for key in a.keys()
             if key not in ignore]
        )

    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(
            [compare_dicts(a_element, b_element, cmps)
             for a_element, b_element in zip(a, b)]
        )

    if type(a) in cmps:
        return cmps[type(a)](a, b)
    return a == b
