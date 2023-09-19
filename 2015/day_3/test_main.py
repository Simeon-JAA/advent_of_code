"""Testing file"""

from main import find_how_many_houses


def test_base_case_1():

    result = find_how_many_houses('^v^v^v^v^v')

    assert result == 2


def test_base_case_2():

    result = find_how_many_houses('^>v<')

    assert result == 4


def test_base_case_3():

    result = find_how_many_houses('^')

    assert result == 2


