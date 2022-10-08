import math
from collections import deque

from pick import pick


def print_directions(directions: deque, distance: int):
    options = ['Go back to main menu', 'Quit program']
    steps = []
    for step, place in enumerate(directions, 1):
        steps.append(str(step) + '. Go to ' + place)
    # 1 step = 0.762 meters
    # (src: https://hextobinary.com/unit/length/from/step/to/meter)
    distance /= 0.762
    distance = math.ceil(distance)
    walking_time = math.ceil(distance / 1)  # hehe
    cycling_time = math.ceil(distance / 5)
    # starting to think that another function should just return the title to this one
    title = '\n'.join(steps) + '\n\n' + str(distance) + ' steps \n' + str(walking_time) + ' secs walking or ' + str(
        cycling_time) + ' secs cycling'
    decision = pick(options, title)[1]  # Get index
    return decision
