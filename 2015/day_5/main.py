"""Advent of Code solution (2015 Day 5)"""


def naughty_or_nice(string: str) -> bool:
    """Returns true if nice and false if naughty"""

    vowels = "aeiou"
    vowel_count = 0

    for letter in string:
        if letter in vowels:
            vowel_count += 1

    if vowel_count < 3:
        return False

    double_letter_count = 0
    for index in range(len(string)-1):
        if string[index] == string[index+1]:
            double_letter_count += 1

    if double_letter_count == 0:
        return False

    not_allowed_strings = {'ab', 'cd', 'pq', 'xy'}

    for letters in not_allowed_strings:
        if letters in string:
            return False

    return True


def naughty_or_nice_p2(string: str) -> bool:
    """Returns true if nice and false if naughty"""

    double_letter_count = 0
    second_condition_count = 0

    for index in range(len(string)):
        if index < len(string) - 1:
            pair = string[index] + string[index + 1]
            print(pair)
            if string.count(pair) >= 2 and double_letter_count == 0:
                double_letter_count += 1
            if index != 0:
                if string[index-1] == string[index+1] and second_condition_count == 0:
                    second_condition_count += 1

    if double_letter_count == 0 or second_condition_count == 0:
        return False

    return True


if __name__ == "__main__":

    nice_people = 0

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            if naughty_or_nice_p2(line):
                nice_people += 1

    print(nice_people)
