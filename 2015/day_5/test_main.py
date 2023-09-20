"""Testing file for main.py (Advent of code 2015 day 5)"""

from main import naughty_or_nice, naughty_or_nice_p2


def test_naughty_or_nice_base_case_1():
    """Tests base case for naughty_or_nice (1st test case)"""

    result = naughty_or_nice("jchzalrnumimnmhp")

    assert result == False


def test_naughty_or_nice_base_case_2():
    """Tests base case for naughty_or_nice (1st test case)"""

    result = naughty_or_nice("haegwjzuvuyypxyu")

    assert result == False


def test_naughty_or_nice_base_case_3():
    """Tests base case for naughty_or_nice (1st test case)"""

    result = naughty_or_nice("dvszwmarrgswjxmb")

    assert result == False


def test_naughty_or_nice_base_case_4():
    """Tests base case for naughty_or_nice (1st test case)"""

    result = naughty_or_nice("ugknbfddgicrmopn")

    assert result == True


def test_naughty_or_nice_base_case_5():
    """Tests base case for naughty_or_nice (1st test case)"""

    result = naughty_or_nice("Simeon")

    assert result == False


def test_naughty_or_nice_p2_base_case_1():
    """Tests base case for naughty_or_nice_p2 (1st test case)"""

    result = naughty_or_nice_p2("qjhvhtzxzqqjkmpb")

    assert result == True


def test_naughty_or_nice_p2_base_case_2():
    """Tests base case for naughty_or_nice_p2 (2nd test case)"""

    result = naughty_or_nice_p2("xxyxx")

    assert result == True


def test_naughty_or_nice_p2_base_case_3():
    """Tests base case for naughty_or_nice_p2 (3rd test case)"""

    result = naughty_or_nice_p2("uurcxstgmygtbstg")

    assert result == False


def test_naughty_or_nice_p2_base_case_4():
    """Tests base case for naughty_or_nice_p2 (4th test case)"""

    result = naughty_or_nice_p2("ieodomkazucvgmuy")

    assert result == False
