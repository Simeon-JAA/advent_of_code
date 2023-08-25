"""Testing file for main"""

from main import fully_overlap_pair, format_input  # Part 1
from main import any_overlap, generate_set  # Part 2


def test_format_input_base_case_1():
    """Tests base case for format_input"""

    result = format_input("2-6,4-8")

    assert result == [[2, 6], [4, 8]]


def test_format_input_base_case_2():
    """Tests base case for format_input"""

    result = format_input("2-10,12-100")

    assert result == [[2, 10], [12, 100]]


def test_fully_overlap_pair_base_case_1():
    """Tests base case for fully_overlap_pair"""

    result = fully_overlap_pair("2-4,6-8")

    assert result == False


def test_fully_overlap_pair_base_case_2():
    """Tests base case for fully_overlap_pair"""

    result = fully_overlap_pair("2-8,3-7")

    assert result == True


def test_fully_overlap_pair_base_case_3():
    """Tests base case for fully_overlap_pair"""

    result = fully_overlap_pair("2-6,4-8")

    assert result == False


def test_fully_overlap_pair_base_case_4():
    """Tests base case for fully_overlap_pair"""

    result = fully_overlap_pair("2-6,4-8")

    assert result == False


def test_fully_overlap_pair_base_case_5():
    """Tests base case for fully_overlap_pair"""

    result = fully_overlap_pair("5-7,7-9")

    assert result == False


def test_fully_overlap_pair_edge_case_1():
    """Tests edge case for fully_overlap_pair"""

    result = fully_overlap_pair("10-5,7-9")

    assert result == True


def test_any_overlap_base_case_1():
    """Tests base case for any_overlap_pairs"""

    result = any_overlap("10-5,7-9")

    assert result == True


def test_any_overlap_base_case_2():
    """Tests base case for any_overlap_pairs"""

    result = any_overlap("10-5,7-9")

    assert result == True


def test_generate_set():
    """Tests base case for generate_set"""

    result = generate_set([7, 10])

    assert result == {7, 8, 9, 10}
