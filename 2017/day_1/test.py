"""Testing file for main"""

from main import get_capatcha_sum, get_capatcha_sum_part_2, get_index_to_check


def test_get_capatcha_sum_base_case_1():
    """Tests base case for get_capatcha_sum (1)"""

    result = get_capatcha_sum("1122")

    assert result == 3


def test_get_capatcha_sum_base_case_2():
    """Tests base case for get_capatcha_sum (2)"""

    result = get_capatcha_sum("1111")

    assert result == 4


def test_get_capatcha_sum_base_case_3():
    """Tests base case for get_capatcha_sum (2)"""

    result = get_capatcha_sum("1234")

    assert result == 0


def test_get_capatcha_sum_base_case_4():
    """Tests base case for get_capatcha_sum (4)"""

    result = get_capatcha_sum("91212129")

    assert result == 9


def test_get_index_to_check_base_case_1():
    """Base case for get_index_to_check (1)"""

    result = get_index_to_check(0, 6)

    assert result == 3


def test_get_index_to_check_base_case_2():
    """Base case for get_index_to_check (2)"""

    result = get_index_to_check(3, 6)

    assert result == 0


def test_get_index_to_check_base_case_3():
    """Base case for get_index_to_check (3)"""

    result = get_index_to_check(8, 10)

    assert result == 3


def test_get_capatcha_sum_part_2_base_case_1():
    """Tests base case for get_capatcha_sum (1)"""

    result = get_capatcha_sum_part_2("1212")

    assert result == 6


def test_get_capatcha_sum_part_2_base_case_2():
    """Tests base case for get_capatcha_sum (2)"""

    result = get_capatcha_sum_part_2("1221")

    assert result == 0


def test_get_capatcha_sum_part_2_base_case_3():
    """Tests base case for get_capatcha_sum (3)"""

    result = get_capatcha_sum_part_2("123425")

    assert result == 4


def test_get_capatcha_sum_part_2_base_case_4():
    """Tests base case for get_capatcha_sum (4)"""

    result = get_capatcha_sum_part_2("123123")

    assert result == 12


# def test_get_capatcha_sum_part_2_edge_case_1():
#     """Tests edge case for get_capatcha_sum (1) odd number"""

#     result = get_capatcha_sum_part_2("2131415")

#     assert result == 4
