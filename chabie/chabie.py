from typing import Dict, List, Tuple, Callable


Key = Tuple(type, Callable)


def compare_dicts(a: Dict, b: Dict,
                  custom_comp: Dict = {}, ingore: List = []) -> bool:

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

    print(custom_comp)
    if type(a) in custom_comp:
        print('Look!')
        return custom_comp[type(a)](a, b)
        # a.__eq__ = custom_comp[type(a)]
    return a == b


# TODO type-based
# TODO key-based
print(
    compare_dicts(
        {'hoge': 'hoge'},
        {'hoge': 'fuga'},
        {type(''): lambda a, b: True}
    )
)
