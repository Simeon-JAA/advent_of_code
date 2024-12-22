"""Testing file for main.py (Advent of code 2024 day 2)"""

from main import format_file, get_multiplication_sum

def test_format_file_base_case_1():
    """Tests base case for format_file"""

    input_file = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))0"
    result = format_file(input_file)

    assert result == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

def test_get_multiplication_sum_base_case_1():
    """Tests base case for get_multiplication_sum"""

    input_file = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))0"
    multiplication_list = format_file(input_file)
    result = get_multiplication_sum(multiplication_list)

    assert result == 161