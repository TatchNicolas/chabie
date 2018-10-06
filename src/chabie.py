from datetime import datetime
from typing import Dict, List, Tuple


def custom_comp(a: Dict, b: Dict, key: List[Tuple] = None) -> bool:

    if type(a) != type(b):
        return False

    if isinstance(a, dict):
        if not all([key in b for key in a.keys()]) and all([key in a for key in b.keys()]):
            return False
        return all([custom_comp(a[key], b[key]) for key in a.keys()])

    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all([custom_comp(a_element, b_element) for a_element, b_element in zip(a, b)])

    return a == b


date = datetime.now()
date_a = date.isoformat()
date_b = date.isoformat()

a = {
    'hoge': 1,
    'fuga': 2,
    'piyo': {
        'foo': date_a,
        'bar': [{'fizz': 'bazz'}, 2, 3, 4, 5],
        'baz': True,
    },
}

b = {
    'hoge': 1,
    'fuga': 2,
    'piyo': {
        'foo': date_b,
        'bar': [{'fizz': 'bazz'}, 2, 3, 4, 5],
        'baz': True,
    },
}

print(a)
print(b)
print(custom_comp(a, b))
