"""Main python file"""


def find_wrapping_paper(input: str) -> int:
    """Find the surface area of dimensions"""
    # 2*l*w + 2*w*h + 2*h*l
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
    # smallest perimeter of any one face
    # cubic feet of volume of the present

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

    with open('2015/day_2/input.txt', 'r') as f:
        box_dimensions = f.read().split('\n')

    amount_of_wrapping_paper = 0
    amount_of_ribbon = 0

    for box in box_dimensions:
        amount_of_wrapping_paper += find_wrapping_paper(box)
        amount_of_ribbon += find_ribbon(box)

    print(amount_of_wrapping_paper, amount_of_ribbon)
