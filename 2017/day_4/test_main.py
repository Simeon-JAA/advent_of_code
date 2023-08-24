"""Testing file for main"""

from main import is_passcode_valid, contains_anagram


def test_is_passcode_valid_base_case_1():
    """Tests base case for is_passcode_valid"""

    assert is_passcode_valid("aa bb cc dd ee")


def test_is_passcode_valid_base_case_2():
    """Tests base case for is_passcode_valid"""

    assert not is_passcode_valid("aa bb cc dd aa")


def test_is_passcode_valid_base_case_3():
    """Tests base case for is_passcode_valid"""

    assert is_passcode_valid("aa bb cc dd aaa")


def test_contains_anagram_base_case_1():
    """Tests base case for icontains_anagram"""

    assert not contains_anagram("abcde fghij")


def test_contains_anagram_base_case_2():
    """Tests base case for icontains_anagram"""

    assert contains_anagram("abcde xyz ecdab")


def test_contains_anagram_base_case_3():
    """Tests base case for icontains_anagram"""

    assert not contains_anagram("iiii oiii ooii oooi oooo")
