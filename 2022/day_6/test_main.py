"""Testing file for main (2022 day 6 )"""

from main import all_distinct_characters, detect_first_marker_part_1, detect_first_marker_part_2


def test_all_distinct_characters_base_case_1():
    """Tests base case for all_distinct_characters"""

    input = "abcdefghijklmnopqrstuvwxyz"

    assert all_distinct_characters(input)


def test_all_distinct_characters_base_case_2():
    """Tests base case for all_distinct_characters"""

    input = "abcde"

    assert all_distinct_characters(input)


def test_all_distinct_characters_base_case_3():
    """Tests base case for all_distinct_characters"""

    input = "sbck"

    assert all_distinct_characters(input)


def test_all_distinct_characters_base_case_4():
    """Tests base case for all_distinct_characters"""

    input = "acad"

    assert not all_distinct_characters(input)


def test_all_distinct_characters_base_case_5():
    """Tests base case for all_distinct_characters"""

    input = "accd"

    assert not all_distinct_characters(input)


def test_all_distinct_characters_base_case_6():
    """Tests base case for all_distinct_characters"""

    input = "dddd"

    assert not all_distinct_characters(input)


def test_all_distinct_characters_base_case_7():
    """Tests base case for all_distinct_characters"""

    input = "aa"

    assert not all_distinct_characters(input)


def test_detect_first_marker_part_1_base_case_1():
    """Base case for function detect_first_marker_part_1"""

    input = "bvwbjplbgvbhsrlpgdmjqwftvncz"

    result = detect_first_marker_part_1(input)

    assert result == 5


def test_detect_first_marker_part_1_base_case_2():
    """Base case for function detect_first_marker_part_1"""

    input = "nppdvjthqldpwncqszvftbrmjlhg"

    result = detect_first_marker_part_1(input)

    assert result == 6


def test_detect_first_marker_part_1_base_case_3():
    """Base case for function detect_first_marker_part_1"""

    input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

    result = detect_first_marker_part_1(input)

    assert result == 10


def test_detect_first_marker_part_1_base_case_4():
    """Base case for function detect_first_marker_part_1"""

    input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    result = detect_first_marker_part_1(input)

    assert result == 11


def test_detect_first_marker_part_2_base_case_1():
    """Base case for function detect_first_marker_part_2"""

    input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    result = detect_first_marker_part_2(input)

    assert result == 19


def test_detect_first_marker_part_2_base_case_2():
    """Base case for function detect_first_marker_part_2"""

    input = "bvwbjplbgvbhsrlpgdmjqwftvncz"

    result = detect_first_marker_part_2(input)

    assert result == 23


def test_detect_first_marker_part_2_base_case_3():
    """Base case for function detect_first_marker_part_2"""

    input = "nppdvjthqldpwncqszvftbrmjlhg"

    result = detect_first_marker_part_2(input)

    assert result == 23


def test_detect_first_marker_part_2_base_case_4():
    """Base case for function detect_first_marker_part_2"""

    input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

    result = detect_first_marker_part_2(input)

    assert result == 29


def test_detect_first_marker_part_2_base_case_5():
    """Base case for function detect_first_marker_part_2"""

    input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    result = detect_first_marker_part_2(input)

    assert result == 26


def test_detect_first_marker_part_2_base_case_4():
    """Base case for function detect_first_marker_part_2"""

    input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

    result = detect_first_marker_part_2(input)

    assert result == 29
