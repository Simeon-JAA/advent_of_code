"""Solution for 2017 day 5"""


def get_input(file_path: str) -> str:
    """Returns input from file input.txt"""

    with open(file_path, "r") as f:
        return f.read()


def how_many_jumps(input: list[int]) -> int:
    """Returns number of jumps required to exit the maze"""

    current_position = 0
    current_jumps = 0
    final_index = len(input) - 1

    while current_position <= final_index:
        prev_position = current_position
        current_position += input[current_position]
        input[prev_position] += 1
        current_jumps += 1

    return current_jumps

# TODO complete pt 2


def how_many_jumps_part_2(input: list[int]) -> int:
    """Returns number of jumps required to exit the maze"""

    original_input = input.copy()

    current_position = 0
    current_jumps = 0
    final_index = len(input) - 1

    while current_position <= final_index:
        prev_position = current_position
        current_position += input[current_position]
        if original_input[prev_position] - input[prev_position] < 3:
            input[prev_position] += 1
        else:
            input[prev_position] -= 1

        current_jumps += 1

    return current_jumps


if __name__ == "__main__":

    input = get_input("2017/day_5/input.txt").split("\n")
    input = list(map(lambda x: int(x), input))

    print(how_many_jumps(input), how_many_jumps_part_2(input))
