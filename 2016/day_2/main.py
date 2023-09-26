"""Solution to Advent of Code 2016 day 2"""


def get_input_data(file_path: str) -> str:
    """Returns input data to use in solution"""
    with open(file_path, "r") as f:
        return f.read()


if __name__ == "__main__":

    input_data = get_input_data("input.txt")

    print(input_data)
