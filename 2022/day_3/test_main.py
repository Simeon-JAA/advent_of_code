"""Testing file for main"""

from main import create_letter_priorities, sum_priority, find_common_items


def test_create_letter_priorities():
    """Tests base case for create_letter_priorities"""

    answer = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
              'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
              'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
              'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
              'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
              'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30,
              'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35,
              'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
              'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
              'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50,
              'Y': 51, 'Z': 52}

    result = create_letter_priorities()

    assert result == answer


def test_sum_priority_base_case_1():
    """Tests base case for sum_priority"""

    input = {"a": 2, "A": 1}

    result = sum_priority(input)

    assert result == 29


def test_sum_priority_base_case_2():
    """Tests base case for sum_priority"""

    input = {"a": 18}

    result = sum_priority(input)

    assert result == 18


def test_sum_priority_base_case_3():
    """Tests base case for sum_priority"""

    input = {"a": 4, "c": 1}

    result = sum_priority(input)

    assert result == 7


def test_sum_priority_base_case_4():
    """Tests base case for sum_priority"""

    input = {"A": 2, "Z": 1}

    result = sum_priority(input)

    assert result == 106


def test_find_common_items_base_case_1():
    """Tests base case for find_common_items"""

    result = find_common_items("vJrwpWtwJgWrhcsFMMfFFhFp")

    assert result == {"p": 1}


def test_find_common_items_base_case_2():
    """Tests base case for find_common_items"""

    result = find_common_items("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")

    assert result == {"L": 1}


def test_find_common_items_base_case_3():
    """Tests base case for find_common_items"""

    result = find_common_items("PmmdzqPrVvPwwTWBwg")

    assert result == {"P": 1}
