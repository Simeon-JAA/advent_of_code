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


def any_overlap(input: str) -> bool:
    """Returns True if any section overlaps with another else False"""
    input = format_input(input)

   pass


if __name__ == "__main__":

    input = get_input("2022/day_4/input.txt").split("\n")

    fully_overlapped_pairs = 0
    any_overlap_pairs = 0 
    for pair in input:
        # Part 1
        if fully_overlap_pair(pair):
            fully_overlapped_pairs += 1
        # Part 2
        if any_overlap(pair):
            any_overlap_pairs += 1

    print(fully_overlapped_pairs, any_overlap_pairs)
