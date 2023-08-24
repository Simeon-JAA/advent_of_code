"""Testing file for main"""


from main import how_many_jumps, how_many_jumps_part_2


def test_how_many_jumps_base_case_1():
    """Tests base case for how_many_jumps"""

    result = how_many_jumps([0, 3, 0, 1, -3])

    assert result == 5


def test_how_many_jumps_part_2_base_case_1():
    """Tests base case for how_many_jumps_part_2"""

    result = how_many_jumps_part_2([0, 3, 0, 1, -3])
    # 2 3 2 3 -1
    assert result == 10
