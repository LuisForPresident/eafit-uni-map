import math
from collections import deque
from pick import pick, Option


def show_directions(directions: deque, distance: int) -> bool:
    directions = join_directions(directions)
    steps = convert_to_steps(distance)
    walking_time = estimate_walking_time(distance)
    title = create_output_title(directions, steps, walking_time)

    options = [
        Option('Go back to main menu', True),
        Option('Quit program', False)
    ]
    decision, index = pick(options, title, indicator='->')
    return decision.value


def join_directions(directions: deque) -> str:
    steps: list = []
    for step, place in enumerate(directions, 1):
        # TODO Create a random message generator
        steps.append(str(step) + '. Go to ' + place)
    steps_str = '\n'.join(steps)
    return steps_str


def create_output_title(steps_str: str,
                        number_of_steps: int,
                        walking_time: int) -> str:
    stats_str = str(number_of_steps) + ' steps \n' + str(walking_time) + ' secs walking'
    final_str = steps_str + '\n\n' + stats_str
    return final_str


def convert_to_steps(distance_in_meters: int) -> int:
    number_of_steps = distance_in_meters / 0.762  # Reference: 1 step = 0.762 meters
    number_of_steps = math.ceil(number_of_steps)  # Round to integer
    return number_of_steps


def estimate_walking_time(distance_in_meters: int) -> int:
    walking_time = distance_in_meters / 1  # TODO Get a better ref for the estimation
    # TODO Ceil the result when previous todo item is ready
    return walking_time
