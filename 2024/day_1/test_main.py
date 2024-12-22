"""Testing file for main.py (Advent of code 2024 day 2)"""

from main import format_file, create_lists, get_list_difference, get_list_similarity


def test_format_file_base_case_1():
    """Tests base case for format_file"""

    input_file = """
1 2
3 4
5 6"""
    result = format_file(input_file)

    assert result == "1 2 3 4 5 6"

def test_format_file_base_case_2():
    """Tests base case for format_file"""

    input_file = """
1 3
3 5
5 65"""
    result = format_file(input_file)

    assert result == "1 3 3 5 5 65"

def test_format_file_base_case_3():
    """Tests base case for format_file"""

    input_file = "     1      3      "
    result = format_file(input_file)

    assert result == "1 3"

def test_format_file_base_case_4():
    """Tests base case for format_file"""

    input_file = "  11112      4445      "
    result = format_file(input_file)

    assert result == "11112 4445"

def test_format_file_base_case_5():
    """Tests base case for format_file"""

    input_file = """  111098      4445      
    12334   33445
    22222 22222     """
    result = format_file(input_file)

    assert result == "111098 4445 12334 33445 22222 22222"

def test_create_lists_base_case_1():
    """Tests base case for create_list"""

    result_1, result_2 = create_lists('1 2 3 4')

    assert result_1 == ['1', '3']
    assert result_2 == ['2', '4']

def test_create_lists_base_case_2():
    """Tests base case for create_list"""

    result_1, result_2 = create_lists('   1    2    3     4   ')

    assert result_1 == ['1', '3']
    assert result_2 == ['2', '4']
    
def test_create_lists_base_case_3():
    """Tests base case for create_list"""

    result_1, result_2 = create_lists('   2    2    5     6   ')

    assert result_1 == ['2', '5']
    assert result_2 == ['2', '6']

def test_create_lists_base_case_4():
    """Tests base case for create_list"""

    result_1, result_2 = create_lists("""   2    2    
                                      5     6 
                                      100 1001  """)

    assert result_1 == ['2', '5', '100']
    assert result_2 == ['2', '6', '1001']
    
def test_create_lists_base_case_5():
    """Tests base case for create_list"""

    result_1, result_2 = create_lists("""   
                                      2    2    
                                      5     6 
                                      100   1001  """)

    assert result_1 == ['2', '5', '100']
    assert result_2 == ['2', '6', '1001']

def test_get_list_difference_base_case_1():
    """Tests base case for get_list_difference"""

    list_1, list_2 = create_lists("""   
                                      1    2    
                                      3     4 
                                      5   6  """)
    
    result = get_list_difference(list_1, list_2)

    assert result == 3

def test_get_list_similarity_base_case_1():
    """Tests base case for get_list_similarity"""

    list_1, list_2, = create_lists("1 1 1 1")
    result = get_list_similarity(list_1, list_2)

    assert result == 4

def test_get_list_similarity_base_case_2():
    """Tests base case for get_list_similarity"""

    list_1, list_2, = create_lists("1 1 2 1")
    result = get_list_similarity(list_1, list_2)

    assert result == 2

def test_get_list_similarity_base_case_3():
    """Tests base case for get_list_similarity"""

    list_1, list_2, = create_lists("0 1 2 1")
    result = get_list_similarity(list_1, list_2)

    assert result == 0

def test_get_list_similarity_base_case_4():
    """Tests base case for get_list_similarity"""

    list_1, list_2, = create_lists("5 1 2 5 6 5")
    result = get_list_similarity(list_1, list_2)

    assert result == 10