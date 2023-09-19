"""Main python file"""


def find_how_many_houses(input: str) -> int:
    """Find the number of houses Santa delivers to"""

    coordinates = {"vertical": 0,
                   "horizontal": 0}

    position_tracking = []

    position_tracking.append(tuple(coordinates.copy().values()))

    for dir in input:
        if dir == "^":
            coordinates["vertical"] += 1
        elif dir == ">":
            coordinates["horizontal"] += 1
        elif dir == "v":
            coordinates["vertical"] -= 1
        elif dir == "<":
            coordinates["horizontal"] -= 1
        coordinates = coordinates
        position_tracking.append(tuple(coordinates.copy().values()))

    position_tracking = set(position_tracking)

    return len(position_tracking)


def find_how_many_houses_2(input: str) -> int:
    """Find the number of houses Santa and robo delivers to"""

    coordinates_santa = {"vertical": 0,
                         "horizontal": 0}
    coordinates_robot = {"vertical": 0,
                         "horizontal": 0}

    position_tracking_santa = []
    position_tracking_robot = []
    position_tracking_santa.append(tuple(coordinates_santa.copy().values()))
    position_tracking_robot.append(tuple(coordinates_robot.copy().values()))

    for index, dir in enumerate(input):
        if index % 2 == 0:
            if dir == "^":
                coordinates_santa["vertical"] += 1
            elif dir == ">":
                coordinates_santa["horizontal"] += 1
            elif dir == "v":
                coordinates_santa["vertical"] -= 1
            elif dir == "<":
                coordinates_santa["horizontal"] -= 1
            coordinates_santa = coordinates_santa
            position_tracking_santa.append(
                tuple(coordinates_santa.copy().values()))
        else:
            if dir == "^":
                coordinates_robot["vertical"] += 1
            elif dir == ">":
                coordinates_robot["horizontal"] += 1
            elif dir == "v":
                coordinates_robot["vertical"] -= 1
            elif dir == "<":
                coordinates_robot["horizontal"] -= 1
            coordinates_robot = coordinates_robot
            position_tracking_robot.append(
                tuple(coordinates_robot.copy().values()))

    # print(len(set(position_tracking_robot)))
    print(position_tracking_santa.extend(position_tracking_robot))

    # return len(set(position_tracking_robot))


if __name__ == "__main__":

    with open('2015/day_3/input.txt', 'r') as f:
        input = f.read()

    print(find_how_many_houses_2(input))
