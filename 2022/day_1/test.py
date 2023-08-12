"""Testing file for day 1 of advent of code 2022"""

from main import get_max_calories, get_total_top_three_calories


def test_get_max_calories_base_case_1():
    """Tests base case for get_max_calories"""

    input = ["10"]
    
    result = get_max_calories(input)

    assert result == 10


def test_get_max_calories_base_case_2():
    """Tests base case for get_max_calories"""

    input = ["10", "10", "10", "10"]
    
    result = get_max_calories(input)

    assert result == 40


def test_get_max_calories_base_case_3():
    """Tests base case for get_max_calories"""

    input = ["10", "10", "", "10"]
    
    result = get_max_calories(input)

    assert result == 20