"""Day 3 of 2024 advent of code"""

import re


def get_file(file_path: str) -> str:
    """Returns input file"""

    with open(file_path, "r") as f:
        return f.read()


def format_file(input_str: str) -> list[str]:
    """Formats file input"""

    multiplication_list = re.findall(r"mul\([0-9]+,[0-9]+\)", input_str)

    return multiplication_list
        

def get_multiplication_sum(multiplication_list: list[str]) -> int:
    """Returns sum of multiplication from list"""
    
    sum = 0 

    for x in multiplication_list:
        numbers = x.replace("mul(", "").replace(")","").split(",")
        sum += int(numbers[0]) *  int(numbers[-1])
    return sum

if __name__ == "__main__":

    input_list = get_file("2024/day_3/input.txt")

    input_list = format_file(input_list)

    multiplication_sum = get_multiplication_sum(input_list)

    print(multiplication_sum)



