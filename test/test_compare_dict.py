from datetime import datetime, timedelta

from chabie import chabie


def test_basics():
    assert chabie.compare_dicts({}, {})
    assert chabie.compare_dicts({'a': ''}, {'a': ''})
    assert not chabie.compare_dicts({'a': ''}, {'b': ''})
    assert not chabie.compare_dicts({'a': ''}, {})
    assert not chabie.compare_dicts({}, {'b': ''})
    assert not chabie.compare_dicts({'a': ''}, None)
    assert not chabie.compare_dicts(None, {'a': ''})
    assert chabie.compare_dicts(
        {
            'int': 0,
            'bool': False,
            'None': None,
            'empty_str': '',
            'empty_list': [],
            'empty_dict': {}
        },
        {
            'int': 0,
            'bool': False,
            'None': None,
            'empty_str': '',
            'empty_list': [],
            'empty_dict': {}
        },
    )
    assert chabie.compare_dicts(
        {
            'nested_list_1': [1, 2, 3],
            'nested_list_2': [
                {'dict_in_list_1': True},
                {'dict_in_list_2': 'foo'},
            ],
            'nested_dict_1': {'key_1': 'value_1'},
            'nested_dict_2': [
                'yi', 'er', 'san'
            ],
        },
        {
            'nested_list_1': [1, 2, 3],
            'nested_list_2': [
                {'dict_in_list_1': True},
                {'dict_in_list_2': 'foo'},
            ],
            'nested_dict_1': {'key_1': 'value_1'},
            'nested_dict_2': [
                'yi', 'er', 'san'
            ],
        }
    )
    assert not chabie.compare_dicts(
        {
            'some list': [1, 2, 3],
            'This key not in the second dict': 'So returns false'
        },
        {
            'some list': [1, 2, 3],
        }
    )
    assert not chabie.compare_dicts(
        {'some list': [1, 2, 3]},
        {'some list': [1, 2, 3, 4]}
    )


def test_keys():
    assert chabie.compare_dicts(
        {'To ignore case': 'or', 'not to ignore': 'That is the question'},
        {'To ignore case': 'OR', 'not to ignore': 'That is the question'},
        keys={'To ignore case': lambda a, b: a.casefold() == b.casefold()}
    )
    assert chabie.compare_dicts(
        {'To ignore': None, 'not to ignore': 'That is the question'},
        {'To ignore': 'None', 'not to ignore': 'That is the question'},
        keys={'To ignore': lambda a, b: True}
    )
    assert chabie.compare_dicts(
        {'assert length of list': [1, 2, 3]},
        {'assert length of list': ['one', 'two', 'three']},
        keys={'assert length of list': lambda a, b: len(a) == len(b)}
    )


def test_types():
    assert chabie.compare_dicts(
        {'strings': 'Given the named argument below'},
        {'strings': 'will be regarded as equal whatever the values are'},
        types={str: lambda a, b: True}
    )
    assert chabie.compare_dicts(
        {
            'int rounded': 6,
            'float rounded': 1.23
        },
        {
            'int rounded': 7,
            'float rounded': 1.23
        },
        types={
            int: lambda a, b: round(a, -1) == round(b, -1),
            float: lambda a, b: round(a) == round(b)
        }
    )
    assert chabie.compare_dicts(
        {'date': datetime(2000, 3, 3, 10, 0, 0)},
        {'date': datetime(2000, 3, 3, 10, 0, 0, 500)},
        # Within a second
        types={datetime: lambda a, b: a-b < timedelta(0, 1)}
    )


def test_ignore():
    assert chabie.compare_dicts(
        {
            'To ignore this key': 'the value does not matter',
            'not to ignore': 'That is the question'
        },
        {
            'even type does not matter': {},
            'not to ignore': 'That is the question'
        },
        ignore=['To ignore this key', 'even type does not matter']
    )
