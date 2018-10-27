from chabie.chabie import compare_dicts


def test_type_based():
    assert compare_dicts({}, {})
