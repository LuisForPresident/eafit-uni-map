import csv
from venv import create
from pick import *
from dijkstra import *


def welcome_user():
    options = ['Go!', 'Edit favorites']
    title = '\nEAFIT University Map - 2022\n'\
            'Luis M. Torres-Villegas & Miguel Suárez-Obando\n'\
            'https://github.com/LuisForPresident/eafit-uni-map/\n\n'\
            'Welcome! Get directions based on some landmarks on campus.'
    return pick(options, title, indicator='->')[1]


def pick_locations(options, first):
    if first is True:
        title = 'Where are you now?'
    else:
        title = 'Where are you going?'

    location = pick(options, title, indicator='->')[0]
    return location


def add_favorites(favorites_path):
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            already_favorites = []
    print(already_favorites)
    all_places = create_options_list('example.csv')
    for place in all_places:
        for favorite in already_favorites:
            if favorite in all_places:
                all_places.remove(favorite)
    try:
        favorites_from_pick = pick(all_places, 'What favorites do you want to add (SPACE AND RETURN)', multiselect=True)
    except ValueError:
        welcome_user()
        # pending: maybe the function itself should not be available if this error occurs?
    else:
        favorites_to_add = []
        for favorite in favorites_from_pick:
            favorites_to_add.append(favorite[0])
        
        favorites_to_add.extend(already_favorites)  # so it doesn't overwrite the existing favorites

        with open(favorites_path, mode='w') as final_favorites:
            csv.writer(final_favorites, delimiter=',').writerow(favorites_to_add)





def edit_favorites(graph_path, options_another):
    title = 'Marca tus destinos favoritos (ESPACIO para marcar, ENTER para confirmar):'
    primera_vez = input('Primera vez? [Y/n]  ')
    if primera_vez == 'Y':
        options = create_options_list(graph_path)
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

def read_favorites():
    with open('favorites.csv', mode='r') as csv_file:
        favorite_reader = csv.reader(csv_file, delimiter=',')
        options = next(favorite_reader)
    return options


def create_options_list(graph_path):
    with open(graph_path) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
        first_row[-1] = first_row[-1].replace(';', '')
    return first_row





def print_directions(directions):
    # pendiente:
    for place in directions:
        print('Ve al nodo', place)


def __init__():
    graph_path = 'example.csv'
    favorites_path = 'favorites.csv'
    time_and_distance_path = 'time_and_distance.csv'
    welcome_user()
    the_list = edit_favorites(graph_path, read_favorites)
    change_favorites(the_list)
    # This itself could be a function
    options = create_options_list(graph_path, read_favorites(graph_path))
    initial_location = pick_locations(options, True)
    options.remove(initial_location)
    final_location = pick_locations(options, False)
    print(f'''\nThe user is at {initial_location} and is going to {final_location}\n''')


# __init__()

add_favorites('favorites.csv')