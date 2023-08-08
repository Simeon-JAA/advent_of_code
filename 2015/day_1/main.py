"""Main python file"""

def find_floor(input: str) -> int:

    """Find floor based on input"""

    bracket_identifier = {
        '(': 1,
        ')': -1
    }
    floor_number = 0 
    index_of_first_basement = 0

    for bracket in input:
        if bracket in bracket_identifier:
            floor_number += bracket_identifier[bracket]

    return floor_number

def find_first_basement_index(input: str) -> int:

    """Find index of string that made santa enter a minus level"""

    bracket_identifier = {
        '(': 1,
        ')': -1
    }
    floor_number = 0 
    index_of_first_basement = 0

    for i, bracket in enumerate(input):
        if bracket in bracket_identifier:
            floor_number += bracket_identifier[bracket]
        if floor_number < 0:
            index_of_first_basement = i + 1
            return index_of_first_basement
    

if __name__ == "__main__":

    with open('2015/day_1/input.txt', 'r') as f:
        floor_identifier = f.read()


    print(find_floor(floor_identifier))
    print(find_first_basement_index(floor_identifier))
