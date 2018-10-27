from typing import Dict


def compare_dicts(a: Dict, b: Dict, key_list: Dict) -> bool:

    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        if not sorted(a.keys()) == sorted(b.keys()):
            return False
        return all(
            [compare_dicts(a[key], b[key], key_list) for key in a.keys()]
        )

    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(
            [
                compare_dicts(a_element, b_element, key_list)
                for a_element, b_element in zip(a, b)
            ]
        )

    print(key_list)
    if type(a) in key_list:
        print('Look!')
        return key_list[type(a)](a, b)
        # a.__eq__ = key_list[type(a)]
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
