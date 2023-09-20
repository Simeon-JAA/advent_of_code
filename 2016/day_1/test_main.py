"""Testing file for main.py (Advent of code 2016 day 1)"""

from main import how_many_blocks_away, determine_direction, determine_position
from main import sum_blocks_away


def test_how_many_blocks_away_base_case_1():
    """Tests base case for how_many_blocks_away"""

    result = how_many_blocks_away(["R2"])

    assert result == 2


def test_how_many_blocks_away_base_case_2():
    """Tests base case for how_many_blocks_away"""

    result = how_many_blocks_away(["R2", "L3"])

    assert result == 5


def test_how_many_blocks_away_base_case_3():
    """Tests base case for how_many_blocks_away"""

    result = how_many_blocks_away(["R0", "L0"])

    assert result == 0


def test_how_many_blocks_away_base_case_4():
    """Tests base case for how_many_blocks_away"""

    result = how_many_blocks_away(["R1", "R1", "R1", "R1"])

    assert result == 0


def test_determine_direction_base_case_1():
    """Tests base case for determine_direction"""

    result = determine_direction("north", "r")

    assert result == "east"


def test_determine_direction_base_case_2():
    """Tests base case for determine_direction"""

    result = determine_direction("south", "r")

    assert result == "west"


def test_determine_direction_base_case_3():
    """Tests base case for determine_direction"""

    result = determine_direction("south", "l")

    assert result == "east"


def test_determine_direction_base_case_4():
    """Tests base case for determine_direction"""

    result = determine_direction("north", "l")

    assert result == "west"


def test_determine_direction_base_case_5():
    """Tests base case for determine_direction"""

    result = determine_direction("west", "r")

    assert result == "north"


def test_determine_position_base_case_1():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 0,
                                 "horizontal": 0},
                                "north",
                                5)

    assert result == {"vertical": 5,
                      "horizontal": 0}


def test_determine_position_base_case_2():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 0,
                                 "horizontal": 0},
                                "east",
                                5)

    assert result == {"vertical": 0,
                      "horizontal": 5}


def test_determine_position_base_case_3():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 0,
                                 "horizontal": 0},
                                "south",
                                2)

    assert result == {"vertical": -2,
                      "horizontal": 0}


def test_determine_position_base_case_4():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 0,
                                 "horizontal": 0},
                                "west",
                                3)

    assert result == {"vertical": 0,
                      "horizontal": -3}


def test_determine_position_base_case_5():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 10,
                                 "horizontal": 0},
                                "north",
                                5)

    assert result == {"vertical": 15,
                      "horizontal": 0}


def test_determine_position_base_case_6():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 10,
                                 "horizontal": 6},
                                "north",
                                5)

    assert result == {"vertical": 15,
                      "horizontal": 6}


def test_determine_position_base_case_7():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 5,
                                 "horizontal": 5},
                                "west",
                                2)

    assert result == {"vertical": 5,
                      "horizontal": 3}


def test_determine_position_base_case_8():
    """Tests base case for determine_position"""

    result = determine_position({"vertical": 5,
                                 "horizontal": 5},
                                "west",
                                7)

    assert result == {"vertical": 5,
                      "horizontal": -2}


def test_sum_blocks_away_base_case_1():
    """Tests base case for sum_blocks_away"""

    result = sum_blocks_away({"vertical": 5,
                              "horizontal": 5})

    assert result == 10


def test_sum_blocks_away_base_case_2():
    """Tests base case for sum_blocks_away"""

    result = sum_blocks_away({"vertical": 1,
                              "horizontal": 1})

    assert result == 2


def test_sum_blocks_away_base_case_3():
    """Tests base case for sum_blocks_away"""

    result = sum_blocks_away({"vertical": 0,
                              "horizontal": -5})

    assert result == 5


def test_sum_blocks_away_base_case_4():
    """Tests base case for sum_blocks_away"""

    result = sum_blocks_away({"vertical": 20,
                              "horizontal": -20})

    assert result == 40


def test_sum_blocks_away_base_case_5():
    """Tests base case for sum_blocks_away"""

    result = sum_blocks_away({"vertical": 0,
                              "horizontal": 0})

    assert result == 0
