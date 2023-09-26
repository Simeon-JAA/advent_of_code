"""Testing file for main.py (Advent of code 2016 day 2)"""

from main import find_keypad_combination, find_next_number


def test_find_keypad_combination_base_case_1():
    """Tests base case for find_keypad_combination"""

    input = ["ULL", "RRDDD", "LURDL", "UUUUD"]

    assert find_keypad_combination(input) == 1985


def test_find_keypad_combination_base_case_2():
    """Tests base case for find_keypad_combination"""

    input = ["U", "L", "RR", "D"]

    assert find_keypad_combination(input) == 2136


def test_find_keypad_combination_base_case_3():
    """Tests base case for find_keypad_combination"""

    input = ["U"]

    assert find_keypad_combination(input) == 2


def test_find_keypad_combination_base_case_4():
    """Tests base case for find_keypad_combination"""

    input = ["U", "DD", "U"]

    assert find_keypad_combination(input) == 285


def test_find_next_number_base_case_1():
    """Tests base case for find_next_number"""

    assert find_next_number("UL", 5) == 1


def test_find_next_number_base_case_2():
    """Tests base case for find_next_number"""

    assert find_next_number("D", 5) == 8


def test_find_next_number_base_case_3():
    """Tests base case for find_next_number"""

    assert find_next_number("DLRR", 5) == 9


def test_find_next_number_base_case_4():
    """Tests base case for find_next_number"""

    assert find_next_number("DDRLRR", 1) == 9


def test_find_next_number_edge_case_1():
    """Tests edge case for find_next_number"""

    assert find_next_number("ULLL", 5) == 1


def test_find_next_number_edge_case_2():
    """Tests edge case for find_next_number"""

    assert find_next_number("UUUUUUUUUUUUU", 5) == 2


def test_find_next_number_edge_case_3():
    """Tests edge case for find_next_number"""

    assert find_next_number("URRRRRRRR", 1) == 3


def test_find_next_number_edge_case_4():
    """Tests edge case for find_next_number"""

    assert find_next_number("LLLLLLL", 5) == 4
