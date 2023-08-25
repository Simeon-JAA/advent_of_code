"""Testing file for main"""

from main import set_empty_stack, update_crate_stack


def test_create_empty_stack_base_case_1():
    """Tests base case for create_empty_stack"""

    result = set_empty_stack("123")

    assert result == {1: [],
                      2: [],
                      3: []}


def test_create_empty_stack_base_case_2():
    """Tests base case for create_empty_stack"""

    result = set_empty_stack("1")

    assert result == {1: []}


def test_create_empty_stack_base_case_3():
    """Tests base case for create_empty_stack"""

    result = set_empty_stack("394")

    assert result == {3: [],
                      4: [],
                      9: []}


def test_create_empty_stack_edge_case():
    """Tests edge for create_empty_stack"""

    result = set_empty_stack("4 9 7        1")

    assert result == {1: [],
                      4: [],
                      7: [],
                      9: []}


def test_update_crate_stack_base_case_1():
    """Tests base case for update_crate_stack"""

    stack = {1: [],
             4: [],
             7: [],
             9: []}

    result = update_crate_stack(stack, [1, "D"])

    assert result == {1: ["D"],
                      4: [],
                      7: [],
                      9: []}


def test_update_crate_stack_base_case_2():
    """Tests base case for update_crate_stack"""

    stack = {1: [], }

    result = update_crate_stack(stack, [1, "D"])

    assert result == {1: ["D"]}


def test_update_crate_stack_base_case_3():
    """Tests base case for update_crate_stack"""

    stack = {1: [],
             5: ["G"],
             9: []}

    result = update_crate_stack(stack, [5, "D"])

    assert result == {1: [],
                      5: ["G", "D"],
                      9: []}
