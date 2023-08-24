"""Solution to 2017 day 1"""


def get_input(file_path: str) -> str:
    """Returns input from file input.txt"""

    with open(file_path, "r") as f:
        return f.read()


def get_capatcha_sum(input: str) -> int:
    """Returns sum of capatcha"""

    total = 0

    for index, num in enumerate(input):
        if index == len(input) - 1:
            if num == input[0]:
                total += int(num)
            continue
        if num == input[index + 1]:
            total += int(num)

    return total


def get_index_to_check(index: int, circle_length: int) -> int:
    """
    Return the position(index) of the input we need to check
    Input is circular and position to check is halfway around the circle
    """
    halfway_away = int(circle_length/2)
    circle_length = circle_length - 1

    new_index = index + halfway_away
    if new_index <= circle_length:
        return new_index
    else:
        new_index = new_index - circle_length - 1
        return new_index


def get_capatcha_sum_part_2(input: str) -> int:
    """Returns sum of capatcha for part 2"""

    total = 0

    input_length = len(input)

    for index, num in enumerate(input):
        index_to_check = get_index_to_check(index, input_length)
        if input[index_to_check] == num:
            total += int(num)

    return total


if __name__ == "__main__":

    input = get_input("2017/day_1/input.txt")
    print(get_capatcha_sum(input))
    print(get_capatcha_sum_part_2(input))
