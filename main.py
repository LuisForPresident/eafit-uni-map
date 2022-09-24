import csv
import logging
from pick import *
from dijkstra import *

""" Declare global paths for csv files
It's more efficient compared with having
an argument in every other function
and having to pass the path every time """
graph_path = 'example.csv'
favorites_path = 'favorites.csv'
time_and_distance_path = 'time_and_distance.csv'


def choose_at_start_menu():
    options = ['Travel', 'Edit favorites']
    title = '\nEAFIT University Map - 2022\n'\
            'Luis M. Torres-Villegas & Miguel Suárez-Obando\n'\
            'https://github.com/LuisForPresident/eafit-uni-map/\n\n'\
            'Welcome! Get directions based on some landmarks on campus.'
    decision = pick(options, title, indicator='->')[1]  # Get the index
    return bool(decision == 0)
    # if decision == 0:  # 'Travel'
    #     return True
    # else:
    #     return False  # 'Edit favorites'
    # https://docs.python.org/3/library/functions.html#bool


def get_location(options: list):
    title = 'Select your current location:'
    location = pick(options, title, indicator='->')[0]
    return location


def choose_from_favorites():
    options = ['From all options', 'From favorites']
    title = 'Choose destination from:'
    decision = pick(options, title, indicator='->')[1]  # Get the index
    if decision == 0:
        return False
    else:
        return True


def get_destination(options: list, location: str):
    if location in options:  # For the favorites special case
        options.remove(location)  # Destination must not be the location
    title = 'Select your destination:'
    destination = pick(options, title, indicator='->')[0]
    return destination


def create_options_list():
    with open(graph_path) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
        first_row[-1] = first_row[-1].replace(';', '')
    return first_row


def create_favorites_list():
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
            return already_favorites
        except StopIteration:
            choose_from_favorites()


def print_directions(directions: deque):
    options = ['Go back to main menu', 'Quit program']
    steps = []
    for step, place in enumerate(directions, 1):
        steps.append(str(step) + '. Go to ' + place)
    title = '\n'.join(steps) + '\n\nAAA steps\nBB secs walking or CC secs biking (pending)'
    decision = pick(options, title)[1]  # Get index
    return decision


def travel():
    location = get_location(create_options_list())
    from_favorites = choose_from_favorites()
    if from_favorites is False:
        destination_list = create_options_list()
    else:
        destination_list = create_favorites_list()
    destination = get_destination(destination_list, location)
    decision = print_directions(get_shortest_path(location, destination))
    if decision == 0:
        procedure()
    else:
        exit()


def add_favorites():
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            already_favorites = []
    logging.debug(already_favorites)
    all_places = create_options_list()
    for place in all_places:
        for favorite in already_favorites:
            if favorite in all_places:
                all_places.remove(favorite)
    try:
        favorites_from_pick = pick(all_places, 'Select favorites to add with SPACE', multiselect=True)
    except ValueError:
        choose_at_start_menu()
        # pending: maybe the function itself should not be available if this error occurs?
    else:
        favorites_to_add = []
        for favorite in favorites_from_pick:
            favorites_to_add.append(favorite[0])

        favorites_to_add.extend(already_favorites)  # so it doesn't overwrite the existing favorites

        with open(favorites_path, mode='w') as final_favorites:
            csv.writer(final_favorites, delimiter=',').writerow(favorites_to_add)


def remove_favorites():
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            choose_at_start_menu()


def edit_favorites(options_another):
    title = 'Marca tus destinos favoritos (ESPACIO para marcar, ENTER para confirmar):'
    primera_vez = input('Primera vez? [Y/n]  ')
    if primera_vez == 'Y':
        options = create_options_list()
    else:
        options = options_another
    selected = pick(options, title, multiselect=True, min_selection_count=0)
    new_list = []
    for option in selected:  # implement later with map()
        new_list.append(option[0])
    return new_list


def change_favorites(list):
    with open('favorites.csv', mode='w') as csv_file:
        favorite_changer = csv.writer(csv_file, delimiter=',')
        favorite_changer.writerow(list)


def read_favorites(favorites_path):
    with open('favorites.csv', mode='r') as csv_file:
        favorite_reader = csv.reader(csv_file, delimiter=',')
        options = next(favorite_reader)
    return options


# Pending: Learn what __main__() and __init__() mean
def procedure():
    if choose_at_start_menu() is True:
        travel()
    else:
        add_favorites()


procedure()
