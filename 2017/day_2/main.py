

def get_input(file_path: str) -> str:
    """Returns input from file input.txt"""

    with open(file_path, "r") as f:
        return f.read()


def format_input(input: str) -> list[int]:
    """Formats string input into a list of integers"""

    input_remove_tabs = input.replace("\t", " ").strip()
    list_input = input_remove_tabs.split(" ")
    list_of_nums_input = list(map(lambda x: int(x), list_input))
    list_of_nums_input.sort()

    return list_of_nums_input


def calculate_difference(input: str) -> int:
    """Calculates the difference between the highest and lowest value in the input"""
    list_nums = format_input(input)

    return list_nums[-1] - list_nums[0]


def get_only_divisible_answer(input: str) -> int:
    """
    Returns the answer to the only divisible two numbers in input
    Must return a whole number (int)
    """

    list_nums = format_input(input)
    list_nums.reverse()
    list_len = len(list_nums)
    for index, num in enumerate(list_nums):
        for comparison_index in range(index + 1, list_len):
            if num % list_nums[comparison_index] == 0:
                return int(num/list_nums[comparison_index])


if __name__ == "__main__":

    input = get_input("2017/day_2/input.txt").split('\n')

    total_part_1 = 0
    total_part_2 = 0

    for row in input:
        total_part_1 += calculate_difference(row)
        total_part_2 += get_only_divisible_answer(row)

    print(total_part_1, total_part_2)
