"""Solution for Advent of Code 2015 day 2"""


def get_input(file_path) -> str:
    """Returns input file to use in code"""

    with open(file_path, 'r') as f:
        return f.read()


def find_wrapping_paper(input: str) -> int:
    """Find the surface area of dimensions"""

    input = list(map(lambda x: int(x), input.split('x')))
    width = input[0]
    height = input[1]
    length = input[2]

    area_1 = width * height
    area_2 = width * length
    area_3 = length * height

    area_list = [area_1, area_2, area_3]
    area_list.sort()

    min_area = area_list[0]

    surface_area = 2 * (area_1 + area_2 + area_3)
    required_wrapping_paper = surface_area + min_area

    return required_wrapping_paper


def find_ribbon(input: str) -> int:
    """Find the amount of ribbon required given the dimensions"""

    input = list(map(lambda x: int(x), input.split('x')))
    width = input[0]
    height = input[1]
    length = input[2]

    perimeter_1 = 2 * (width + height)
    perimeter_2 = 2 * (width + length)
    perimeter_3 = 2 * (length + height)

    list_of_perimeters = [perimeter_1, perimeter_2, perimeter_3]
    list_of_perimeters.sort()
    smallest_perimeter = list_of_perimeters[0]
    volume_of_present = width * height * length

    return smallest_perimeter + volume_of_present


if __name__ == "__main__":

    input_data = get_input("input.txt")
    box_dimensions = input_data.split("\n")

    amount_of_wrapping_paper = 0
    amount_of_ribbon = 0

    for box in box_dimensions:
        amount_of_wrapping_paper += find_wrapping_paper(box)
        amount_of_ribbon += find_ribbon(box)

    print(amount_of_wrapping_paper, amount_of_ribbon)
