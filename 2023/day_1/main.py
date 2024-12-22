"""Day 1 of 2023 advent of code"""

import re

def get_file(file_path: str) -> str:
    """Returns input file"""

    with open(file_path, "r") as f:
        return f.read()

def get_number(text: str) -> int:
    """Retruns first and last digit in text"""
    
    numbers = [t for t in text if t.isnumeric()]

    return int(numbers[0] + numbers[-1])

def get_number_v2(text: str) -> int:
    """Retruns first and last digit in text"""
    
    pass

if __name__ == "__main__":

    input_list = get_file("2023/day_1/input.txt")
    input_list = input_list.split("\n")

    sum = 0
    for item in input_list:
        sum += get_number(item)

    print(sum)