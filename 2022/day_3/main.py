"""Solution for 2022 day 3"""


def get_input(file_name: str) -> str:
    """Returns input"""
    with open(file_name, "r") as f:
        return f.read()


def create_letter_priorities() -> dict:
    """Returns letter priorities"""

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = lower_case.upper()

    letter_prioritisation = {}

    for letter in lower_case:
        letter_prioritisation[letter] = lower_case.find(letter) + 1
    for letter in upper_case:
        letter_prioritisation[letter] = upper_case.find(letter) + 27

    return letter_prioritisation


def sum_letter_count(letter_count: dict) -> int:
    """Returns the sum of the priorities for the given letter count"""

    letter_priotiries = create_letter_priorities()

    total = 0

    for letter in letter_count:
        total += (letter_count[letter] * letter_priotiries[letter])

    return total


def find_common_items(string: str) -> dict:
    """Returns dictionary with common items and amounts"""

    common_letter_count = {}

    center_index = int(len(string)/2)
    first_compartment = set(string[:center_index])
    second_compartment = set(string[center_index:])

    for letter in first_compartment:
        if letter in second_compartment:
            if not common_letter_count:
                common_letter_count[letter] = 0
            common_letter_count[letter] += 1

    return common_letter_count


def find_common_items_in_group(items: list[str]) -> dict:
    """Returns dictionary with common items and amounts"""

    common_letter_count = {}

    bag_1 = set(items[0])
    bag_2 = set(items[1])
    bag_3 = set(items[2])

    for letter in bag_1:
        if letter in bag_2 and letter in bag_3:
            if not common_letter_count:
                common_letter_count[letter] = 0
            common_letter_count[letter] += 1

    return common_letter_count


def update_letter_count(letter_count: dict, new_letter: dict) -> dict:
    """Updates letter count and returns dictionary"""

    current_letter = list(new_letter.keys())[0]

    if current_letter in letter_count:
        letter_count[current_letter] += 1
    else:
        letter_count.update(new_letter)

    return letter_count


if __name__ == "__main__":

    input = get_input("2022/day_3/input.txt")

    input = input.split("\n")

    letter_count = {}
    letter_count_part_2 = {}

    bag_groups = []

    for row in input:
        # Part 1
        letter_count = update_letter_count(
            letter_count, find_common_items(row))
        # Part 2
        bag_groups.append(row)
        if len(bag_groups) == 3:
            letter_count_part_2 = update_letter_count(
                letter_count_part_2, find_common_items_in_group(bag_groups))
            bag_groups = []

    print(sum_letter_count(letter_count))  # Part 1 Answer
    print(sum_letter_count(letter_count_part_2))  # Part 2 Answer
