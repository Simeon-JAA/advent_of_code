"""Testing file for day 2 advent of code"""


from main import determine_score, determine_score_decrypted


def determine_score_base_case_1():
    """Base case 1 for determine_score"""

    assert determine_score("A Y") == 8


def determine_score_base_case_2():
    """Base case 2 for determine_score"""

    assert determine_score("B X") == 1


def determine_score_base_case_3():
    """Base case 3 for determine_score"""

    assert determine_score("C Z") == 6


def determine_score_edge_case_1():
    """Edge case for determine_score"""

    assert determine_score("  C   Z  ") == 6


def determine_score_edge_case_2():
    """Edge case for determine_score"""

    assert determine_score("  cZ ") == 6


def determine_score_edge_case_3():
    """Edge case for determine_score"""

    assert determine_score("  ay ") == 8


def determine_score_decrypted_base_case_1():
    """Base case for determine_score_decrypted"""

    assert determine_score("  ay ") == 4