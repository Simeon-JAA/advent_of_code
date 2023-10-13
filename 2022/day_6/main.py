"""2022 Day 6 Solution"""


def get_input(file_path: str) -> str:
    """Returns input from file input.txt"""

    with open(file_path, "r") as f:
        return f.read()


def all_distinct_characters(character_input: str) -> bool:
    """Returns true if all characters in character input are distinct and false if they are not"""

    for character in character_input:
        if character_input.count(character) > 1:
            return False

    return True


def detect_first_marker_part_1(puzzle_input: str) -> int:
    """Return index of the first marker from the puzzle input (4 distinct characters)"""

    marker_to_test = ""

    for index, character in enumerate(puzzle_input):
        marker_to_test += character

        if len(marker_to_test) > 4:
            last_four_characters = marker_to_test[-5:-1]
            if all_distinct_characters(last_four_characters):
                return index


def detect_first_marker_part_2(puzzle_input: str) -> int:
    """Return index of the first marker from the puzzle input (14 distinct characters)"""

    marker_to_test = ""

    for index, character in enumerate(puzzle_input):
        marker_to_test += character

        if len(marker_to_test) > 14:
            last_fifteen_characters = marker_to_test[-15:-1]
            if all_distinct_characters(last_fifteen_characters):
                return index


if __name__ == "__main__":

    input = get_input("input.txt")

    first_marker_index_part_1 = detect_first_marker_part_1(input)
    first_marker_index_part_2 = detect_first_marker_part_2(input)

    print(first_marker_index_part_1)
    print(first_marker_index_part_2)
