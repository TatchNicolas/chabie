from chabie import chabie


def test_compare_dicts():
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
            'nested_list_1': [1, 2, 3],
            'nested_list_2': [
                {'dict_in_list_1': True},
                {'dict_in_list_2': 'foo'},
            ],
            'nested_dict_1': {'key_1': 'value_1'},
            'nested_dict_2': [
                'yi', 'er', 'san'
            ],
            'This key not in the second dict': 'So returns false'
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
