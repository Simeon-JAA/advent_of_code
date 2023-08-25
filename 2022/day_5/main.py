"""2022 Day 4 Solution"""

import re


def get_input(file_path: str) -> str:
    """Returns input from file input.txt"""

    with open(file_path, "r") as f:
        return f.read()


def set_empty_stack(stack_list: list[str]) -> dict:
    """Creates empty stack of crates given the list stack input"""

    stack_list = stack_list.strip()
    stack_list = stack_list.replace(" ", "")
    stack_list = list(stack_list)
    stack_list.sort()

    empty_stack_dict = {}

    for stack_num in stack_list:
        empty_stack_dict[int(stack_num)] = list()

    return empty_stack_dict


def update_crate_stack(crate_stack: dict, data: list) -> dict:
    """Updates the crate stack and return it"""

    stack = data[0]
    crate = data[-1]

    crate_stack[int(stack)].append(crate)

    return crate_stack


def get_stack_numbers_and_index(string: str) -> dict:
    """Returns dictionary with the number of the stack, and the index to check for content"""

    stack_number_and_index = {}

    for i, stack_num in enumerate(string):
        if stack_num.isnumeric():
            stack_number_and_index[i] = stack_num

    return stack_number_and_index


def generate_crate_stack(list_input: list[str]) -> list:
    """Generate stacks from given input (the long way)"""

    stack_numbers = list_input[-1]
    crate_stack = set_empty_stack(stack_numbers)

    crate_input = list_input[:-1]
    crate_input.reverse()

    stack_number_and_index = get_stack_numbers_and_index(stack_numbers)
    index_to_check = list(stack_number_and_index.keys())

    for row in crate_input:
        for i in index_to_check:
            if row[i].isalpha():
                crate_stack = update_crate_stack(
                    crate_stack, [stack_number_and_index[i], row[i]])

    return crate_stack


if __name__ == "__main__":

    input = get_input("2022/day_5/input.txt").split("\n")

    stack_input = input[0:9]

    crate_stack = generate_crate_stack(stack_input)

    # To see input
    # for row in crate_stack.items():
    #     print(row)
