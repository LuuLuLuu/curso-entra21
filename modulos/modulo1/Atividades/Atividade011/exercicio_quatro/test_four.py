from four import string_length


def test_string():
    assert string_length("0123456789") == 10;


def test_string_wrong():
    assert string_length("0123456789") == 9;
