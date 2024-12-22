"""Day 2 of 2024 advent of code"""

import re

def get_file(file_path: str) -> str:
    """Returns input file"""

    with open(file_path, "r") as f:
        return f.read()


def format_file(input_str: str) -> list[int]:
    """Formats file input"""

    input_str = re.sub(" +", " ", input_str)

    input_list = input_str.split("\n")

    input_list = [r.strip() for r in input_list if r!= '']

    return input_list


def is_report_safe(report_str: str) -> bool:
    """Returns true if report is safe, false if not"""

    report_list = [int(r) for r in report_str.split(" ")]

    previous_number = report_list[0]
    increase_count = 0
    decrease_count = 0

    for i in range(1, len(report_list)):
      
      difference = abs(previous_number - report_list[i])

      if not 1 <= difference <= 3:
          return False

      if report_list[i] < previous_number:
          decrease_count += 1
          previous_number = report_list[i]
          continue

      if report_list[i] > previous_number:
          increase_count += 1
          previous_number = report_list[i]
          continue

    if increase_count !=0 and decrease_count !=0:
        return False        

    return True


def get_safe_reports(report_list: list[str]) -> int:
    """Returns number of safe reports"""
    
    safe_report_counter = 0
    
    for report in report_list:
        if is_report_safe(report) == True:
            safe_report_counter += 1

    return safe_report_counter

if __name__ == "__main__":

    input_list = get_file("2024/day_2/input.txt")

    input_list = format_file(input_list)

    safe_reports = get_safe_reports(input_list)

    print(safe_reports) 

