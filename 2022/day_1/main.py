"""Day 1 of 2022 advent of code"""


def get_file() -> list[int]:
    """Formats the input to a list of all elves with calories"""
    with open('2022\day_1\input.txt', "r") as f:
        return f.read()


def get_max_calories(list_of_calories: list[str]) -> int:
    """Returns the maximum calories per elf"""

    calories_per_elf = []

    calorie_count = 0 

    for number in list_of_calories:
        if number != '':
            calorie_count += int(number)
        else:
            calories_per_elf.append(calorie_count)
            calorie_count = 0

    return max(calories_per_elf)


def get_total_top_three_calories(list_of_calories: list[str]) -> int:
    """Returns the sum of the top 3 calories"""

    calories_per_elf = []

    calorie_count = 0 

    for number in list_of_calories:
        if number != '':
            calorie_count += int(number)
        else:
            calories_per_elf.append(calorie_count)
            calorie_count = 0

    calories_per_elf.sort(reverse=True)
    
    top_three_calories = calories_per_elf[:3]
    
    return sum(top_three_calories)
    

if __name__ =="__main__":


    file = get_file()

    list_of_calories = file.split('\n')
    
    max_calories = get_max_calories(list_of_calories)
    top_three_calories = get_total_top_three_calories(list_of_calories)
    
    print(max_calories, top_three_calories)
