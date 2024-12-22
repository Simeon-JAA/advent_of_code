"""Testing file for main.py (Advent of code 2024 day 2)"""

from main import get_number, get_number_v2


def test_get_number_base_case_1():
    """Tests base case for get_number"""

    result = get_number("1abc2")

    assert result == 12

def test_get_number_base_case_2():
    """Tests base case for get_number"""

    result = get_number("pqr3stu8vwx")

    assert result == 38

def test_get_number_base_case_3():
    """Tests base case for get_number"""

    result = get_number("treb7uchet")

    assert result == 77

def test_get_number_v2_base_case_1():
    """Tests base case for get_number_v2"""

    result = get_number_v2("two1nine")

    assert result == 29

def test_get_number_v2_base_case_2():
    """Tests base case for get_number_v2"""

    result = get_number_v2("eightwothree")

    assert result == 83

def test_get_number_v2_base_case_3():
    """Tests base case for get_number_v2"""

    result = get_number_v2("abcone2threexyz")

    assert result == 13
