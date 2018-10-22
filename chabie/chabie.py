from typing import Dict, List, Tuple


def compare_dicts(a: Dict, b: Dict, key_list: List[Tuple] = None) -> bool:

    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        if not sorted(a.keys()) == sorted(b.keys()):
            return False
        return all([compare_dicts(a[key], b[key]) for key in a.keys()])

    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(
            [
                compare_dicts(a_element, b_element)
                for a_element, b_element in zip(a, b)
            ]
        )

    return a == b
