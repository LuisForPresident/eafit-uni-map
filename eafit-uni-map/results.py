"""
Formats the output of the shortest path algorithm.
"""

from math import ceil
from random import choice

from pick import pick, Option


def show_directions(directions: list, stats: str) -> bool:
    """Displays directions and prompts user: 1) main menu or 2) quit."""
    formatted_directions: str = join_directions(directions)
    title: str = f"{formatted_directions}\n\n{stats}"

    options = [Option("Go back to main menu", True), Option("Quit program", False)]
    decision, _ = pick(options, title, indicator="->")
    return decision.value


def join_directions(directions: list) -> str:
    """Converts list of directions into a formatted string."""
    steps: list = []
    message: str
    options = [
        ". Go to ",
        ". Follow ",
        ". Continue through ",
        ". Walk till you see ",
        ". Stop to contemplate ",
    ]
    header = f"From {directions[0]} to {directions[len(directions) - 1]}\n\n"

    for step, place in enumerate(directions, 1):
        if step == 1:
            message = ". Start from "
        elif step == len(directions):
            message = ". Arrive at "
        else:
            message = choice(options)
        steps.append(str(step) + message + place)
    formatted_directions = "\n".join(steps)
    return header + formatted_directions


def convert_meters_to_steps(distance_in_meters: int) -> int:
    """Converts meters to steps."""
    number_of_steps = distance_in_meters / 0.762  # Reference: 1 step = 0.762 meters
    number_of_steps = ceil(number_of_steps)  # Round to integer
    return number_of_steps


def estimate_walking_time(distance_in_meters: int) -> int:
    """Estimates walking time from walking distance."""
    walking_time = distance_in_meters / 1.788
    walking_time = ceil(walking_time)
    return walking_time
