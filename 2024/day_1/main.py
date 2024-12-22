"""Day 1 of 2024 advent of code"""

import re

def get_file(file_path: str) -> str:
    """Returns input file"""

    with open(file_path, "r") as f:
        return f.read()


def format_file(file_input: str) -> str:
    """Formats file input"""

    file_input = re.sub("\n", " ", file_input)
    file_input = re.sub(" +", " ", file_input) 
    file_input = file_input.strip()

    return  file_input


def create_lists(input_list: str) -> list[str]:
    """Returns two lists """

    input_list = format_file(input_list)

    left_list = []
    right_list = []

    counter = 1

    for list_item in input_list.split(" "):
      if counter % 2 != 0:
          left_list.append(list_item)
          counter +=1
          continue
      if counter % 2 == 0:
          right_list.append(list_item)
          counter +=1
          continue
        
    return left_list, right_list


def get_list_difference(list_1: list[str], list_2: list[str]) -> int:
    """Returns difference between two lists"""
    
    list_1.sort()
    list_2.sort()

    absolute_difference = 0

    for i in range(0, len(list_1)):

      absolute_difference += abs(int(list_1[i]) - int(list_2[i]))
    
    return absolute_difference



def get_list_similarity(list_1: list[str], list_2: list[str]) -> int:
    """Returns list similarity"""
    
    list_similarity = 0
    
    for n in list_1:
        list_similarity += (int(n) * list_2.count(n))
    
    return list_similarity


if __name__ == "__main__":

    input_list = get_file("2024/day_1/input.txt")

    list_1, list_2 = create_lists(input_list)
    
    list_difference = get_list_difference(list_1, list_2)
    list_similarity = get_list_similarity(list_1, list_2)
    
    print(list_difference, list_similarity)
    

