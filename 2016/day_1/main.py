"""Solution to Advent of Code 2016 day 1"""


def get_input_data(file_path: str) -> str:
    """Returns input data to use in solution"""
    with open(file_path, "r") as f:
        return f.read()


def determine_direction(current_direction: str, input: str) -> str:
    """Returns direction to follow based on current direction and input"""

    compass = ["north", "east", "south", "west"]

    if current_direction.lower() == "north" and input.lower() == "l":
        return compass[-1]

    if current_direction.lower() == "west" and input.lower() == "r":
        return compass[0]

    if input.lower() == "l":
        return compass[compass.index(current_direction.lower()) - 1]

    return compass[compass.index(current_direction.lower()) + 1]


def determine_position(current_position: dict, direction: str, amount: int) -> dict:
    """Determines new position based on current position and instructions for new position"""

    if direction.lower() == "north":
        current_position["vertical"] = current_position["vertical"] + amount
        return current_position

    if direction.lower() == "east":
        current_position["horizontal"] = current_position["horizontal"] + amount
        return current_position

    if direction.lower() == "south":
        current_position["vertical"] = current_position["vertical"] - amount
        return current_position

    current_position["horizontal"] = current_position["horizontal"] - amount

    return current_position


def sum_blocks_away(position: dict) -> int:
    """Returns the amount of blocks away and accounts for negative numbers"""

    blocks_away = 0

    coordinates = list(position.values())

    for num in coordinates:
        blocks_away += abs(num)

    return blocks_away


def how_many_blocks_away(directions: list[str]) -> int:
    """Returns blocks away from initial position based on direction input"""

    position = {"vertical": 0, "horizontal": 0}
    current_direction = "north"

    for move in directions:
        new_direction = move[0]
        amount = int(move[1:])

        current_direction = determine_direction(
            current_direction, new_direction)

        position = determine_position(position, current_direction, amount)

    blocks_away = sum_blocks_away(position)

    return blocks_away


if __name__ == "__main__":

    input_data = get_input_data("input.txt")

    directions = input_data.split(", ")

    blocks_away = how_many_blocks_away(directions)

    print(blocks_away)
