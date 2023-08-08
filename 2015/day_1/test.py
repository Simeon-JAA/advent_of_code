"""Testing file"""

from main import find_floor

def test_base_case_1():

    result = find_floor('()()')

    assert result == 0


def test_base_case_2():

    result = find_floor('(()(()(')

    assert result == 3


def test_base_case_3():

    result = find_floor('))(')

    assert result == -1