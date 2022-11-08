import math
from pick import pick, Option
from random import choice, random


def show_directions(directions: list, stats: str) -> bool:
    directions = join_directions(directions)
    title = create_output_title(directions, stats)

    options = [
        Option('Go back to main menu', True),
        Option('Quit program', False)
    ]
    decision, index = pick(options, title, indicator='->')
    return decision.value


def join_directions(directions: list) -> str:
    steps: list = []
    message: str
    options = [
        '. Go to ',
        '. Follow ',
        '. Continue through ',
        '. Walk till you see ',
        '. Stop to contemplate '
    ]
    places_str = 'From {} to {}\n\n'.format(
        directions[0],
        directions[len(directions)-1])

    for step, place in enumerate(directions, 1):
        if step == 1:
            message = '. Start from '
        elif step == len(directions):
            message = '. Arrive at '
        else:
            message = choice(options)
        steps.append(str(step) + message + place)
    steps_str = '\n'.join(steps)
    return places_str + steps_str


def create_output_title(directions_str: str, stats_str: str) -> str:
    final_str = directions_str + '\n\n' + stats_str
    return final_str


def convert_meters_to_steps(distance_in_meters: int) -> int:
    number_of_steps = distance_in_meters / 0.762  # Reference: 1 step = 0.762 meters
    number_of_steps = math.ceil(number_of_steps)  # Round to integer
    return number_of_steps


def estimate_walking_time(distance_in_meters: int) -> int:
    walking_time = distance_in_meters / 1.788
    walking_time = math.ceil(walking_time)
    return walking_time


def get_formatted_stats(steps, walking_time) -> str:
    distance = str(steps)
    timespan: int = walking_time

    formatted_time: str

    if timespan != 0:
        minutes = int(timespan / 60)
        seconds = int(timespan % 60)
        if minutes >= 1:
            formatted_time = '{0} mins and {1} secs'.format(minutes, seconds)
        else:
            formatted_time = '{0} secs'.format(seconds)
    else:
        formatted_time = '0 secs'

    formatted_stats: str = '{0} steps in {1}'.format(distance, formatted_time)

    return formatted_stats
