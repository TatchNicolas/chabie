from typing import Dict, List, Tuple, Callable


Key = List[Tuple[type, Callable]]
Ignore = List[str]


# TODO What if a key only exists in one of given dicts?
def compare_dicts(a: Dict, b: Dict,
                  custom_comp: Key = [], ingore: Ignore = []) -> bool:

    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        if not sorted(a.keys()) == sorted(b.keys()):
            return False
        return all(
            [compare_dicts(a[key], b[key], custom_comp) for key in a.keys()]
        )

    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(
            [
                compare_dicts(a_element, b_element, custom_comp)
                for a_element, b_element in zip(a, b)
            ]
        )

    if type(a) in custom_comp:
        return custom_comp[type(a)](a, b)
    return a == b
