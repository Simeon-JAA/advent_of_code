"""Solution for 2017 day 4"""


def get_input(file_path: str) -> str:
    """Returns input from file input.txt"""

    with open(file_path, "r") as f:
        return f.read()


def is_passcode_valid(string: str) -> bool:
    """Returns true if the passcode is valid and false if not"""

    string = string.split(" ")

    for phrase in string:
        if string.count(phrase) > 1:
            return False

    return True


def contains_anagram(string: str) -> bool:
    """Returns True is password contains anagram and False if not """

    string = string.split(" ")

    letter_counts = []

    for phrase in string:
        letter_count = {}
        letters = set(phrase)

        for letter in letters:
            letter_count[letter] = phrase.count(letter)

        letter_counts.append(letter_count)

    for sets in letter_counts:
        if letter_counts.count(sets) > 1:
            return True

    return False


if __name__ == "__main__":

    input = get_input("2017/day_4/input.txt")
    input = input.split("\n")

    total_part_1 = 0
    total_part_2 = 0

    for row in input:
        if is_passcode_valid(row):
            total_part_1 += 1
        if not contains_anagram(row):
            total_part_2 += 1

    print(total_part_1, total_part_2)
