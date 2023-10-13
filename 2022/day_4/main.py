"""2022 Day 4 Solution"""


def get_input(file_path: str) -> str:
    """Returns input from file input.txt"""

    with open(file_path, "r") as f:
        return f.read()


def format_input(string: str) -> list[list[int]]:
    """Formats string input to a list of integers"""
    split_string = string.split(",")

    split_string = list(map(lambda x: x.split("-"), split_string))

    list_to_return = list(
        map(lambda x: list(map(lambda y: int(y), x), ), split_string))

    return list_to_return


def fully_overlap_pair(input: str) -> bool:
    """Returns True if one section is fully overlapped within another"""
    input = format_input(input)

    elf_1 = input[0]
    elf_1.sort()
    elf_2 = input[-1]
    elf_2.sort()

    elf_1_lowest = elf_1[0]
    elf_1_highest = elf_1[-1]
    elf_2_lowest = elf_2[0]
    elf_2_highest = elf_2[-1]

    if elf_1_lowest <= elf_2_lowest and elf_1_highest >= elf_2_highest:
        return True
    if elf_2_lowest <= elf_1_lowest and elf_2_highest >= elf_1_highest:
        return True
    return False


def generate_set(pair: list[int]) -> set:
    """Generate set from pair input"""

    lower_bound = pair[0]
    upper_bound = pair[-1] + 1

    set_to_return = set()

    for number in range(lower_bound, upper_bound):
        set_to_return.add(number)

    return set_to_return


def any_overlap(input: str) -> bool:
    """Returns True if any section overlaps with another else False"""
    input = format_input(input)

    pair_1 = input[0]
    pair_1.sort()
    pair_1 = generate_set(pair_1)
    pair_2 = input[-1]
    pair_2.sort()
    pair_2 = generate_set(pair_2)

    for num in pair_1:
        if num in pair_2:
            return True

    return False


if __name__ == "__main__":

    input = get_input("input.txt").split("\n")

    fully_overlapped_pairs = 0
    any_overlap_pairs = 0
    for pair in input:
        # Part 1
        if fully_overlap_pair(pair):
            fully_overlapped_pairs += 1
        # Part 2
        if any_overlap(pair):
            any_overlap_pairs += 1

    print(f"Fully overlapped pairs = {fully_overlapped_pairs}")
    print(f"Any overlapped pairs = {any_overlap_pairs}")
