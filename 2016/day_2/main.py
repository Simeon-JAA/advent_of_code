"""Solution to Advent of Code 2016 day 2"""


def get_input_data(file_path: str) -> str:
    """Returns input data to use in solution"""
    with open(file_path, "r") as f:
        return f.read()


def find_keypad_combination(data: list[str]) -> int:
    """Returns keypad combination based on data input"""

    current_number = 5
    keypad_combination = ""

    for step in data:
        current_number = find_next_number(step, current_number)
        keypad_combination += str(current_number)

    return int(keypad_combination)


def find_next_number(instructions: str, current_number: int) -> int:
    """Returns next number on keypad based on instructions provided and current number"""

    keypad_range = range(1, 10)
    direction_association = {"U": -3, "L": -1, "D": 3, "R": 1}
    right_bound = {3, 6, 9}
    left_bound = {1, 4, 7}

    instructions = instructions.upper()

    for letter in instructions:
        if current_number in right_bound and letter == "R":
            continue
        if current_number in left_bound and letter == "L":
            continue
        if current_number + direction_association[letter] not in keypad_range:
            continue
        current_number += direction_association[letter]

    return current_number


if __name__ == "__main__":

    input_data = get_input_data("input.txt")

    input_data = input_data.split("\n")

    print(find_keypad_combination(input_data))
