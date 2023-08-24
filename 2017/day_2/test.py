"""Testing file for main"""

from main import calculate_difference, get_only_divisible_answer


def test_calculate_difference_base_case_1():
    """Base case for calculate_difference"""
    result = calculate_difference("5 1 9 5")

    assert result == 8


def test_calculate_difference_base_case_2():
    """Base case for calculate_difference"""

    result = calculate_difference("7 5 3")

    assert result == 4


def test_calculate_difference_base_case_3():
    """Base case for calculate_difference"""

    result = calculate_difference("2 4 6 8")

    assert result == 6


def test_get_only_divisible_answer_base_case_1():
    """Base case test for get_only_divisible_answer"""

    result = get_only_divisible_answer("5 9 2 8")

    assert result == 4


def test_get_only_divisible_answer_base_case_2():
    """Base case test for get_only_divisible_answer"""

    result = get_only_divisible_answer("9 4 7 3")

    assert result == 3


def test_get_only_divisible_answer_base_case_3():
    """Base case test for get_only_divisible_answer"""

    result = get_only_divisible_answer("3 8 6 5")

    assert result == 2
