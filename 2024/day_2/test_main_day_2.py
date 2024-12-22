"""Testing file for main.py (Advent of code 2024 day 2)"""

from main import format_file, is_report_safe, get_safe_reports

def test_format_file_base_case_1():
    """Tests base case for format_file"""

    input_file = """8 11 14 16 15
23 25 27 30 30"""
    result = format_file(input_file)

    assert result == ["8 11 14 16 15", "23 25 27 30 30"]

def test_format_file_base_case_2():
    """Tests base case for format_file"""

    input_file = """1 2 3 4 5
6 7 8 9 10"""
    result = format_file(input_file)

    assert result == ["1 2 3 4 5", "6 7 8 9 10"]

def test_format_file_base_case_3():
    """Tests base case for format_file"""

    input_file = """
1 2 3 4 5
6 7 8 9 10"""
    result = format_file(input_file)

    assert result == ["1 2 3 4 5", "6 7 8 9 10"]

def test_format_file_base_case_4():
    """Tests base case for format_file"""

    input_file = """
1 2 
6 7 """
    result = format_file(input_file)

    assert result == ["1 2", "6 7"]

def test_is_report_safe_base_case_1():
    """Tests base case for is_report_safe"""

    result = is_report_safe("7 6 4 2 1")

    assert result == True

def test_is_report_safe_base_case_2():
    """Tests base case for is_report_safe"""

    result = is_report_safe("1 2 7 8 9")

    assert result == False

def test_is_report_safe_base_case_3():
    """Tests base case for is_report_safe"""

    result = is_report_safe("9 7 6 2 1")

    assert result == False

def test_is_report_safe_base_case_4():
    """Tests base case for is_report_safe"""

    result = is_report_safe("1 3 2 4 5")

    assert result == False

def test_is_report_safe_base_case_5():
    """Tests base case for is_report_safe"""

    result = is_report_safe("8 6 4 4 1")

    assert result == False

def test_is_report_safe_base_case_6():
    """Tests base case for is_report_safe"""

    result = is_report_safe("1 3 6 7 9")

    assert result == True

def test_get_safe_reports_base_case_1():
    """Tests base case for get_safe_reports"""

    reports = format_file("""7 6 4 2 1
      1 2 7 8 9
      9 7 6 2 1
      1 3 2 4 5
      8 6 4 4 1
      1 3 6 7 9""")

    result = get_safe_reports(reports)

    assert result == 2