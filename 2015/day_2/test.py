"""Testing file"""

from main import find_ribbon

def test_base_case_1():

    result = find_ribbon('2x3x4')

    assert result == 34


