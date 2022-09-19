import csv
from pick import *
from dijkstra import *


def welcome_user():
    options = ["Go!", "Edit favorites"]
    title = "\nEAFIT University Map - 2022\n"\
            "Luis M. Torres-Villegas & Miguel Suárez-Obando\n"\
            "https://github.com/LuisForPresident/eafit-uni-map/\n\n"\
            "Welcome! Get directions based on some landmarks on campus."
    return pick(options, title, indicator='->')[1]


def pick_locations(options, first):
    if first:
        title = "Where are you now?"
    else:
        title = "Where are you going?"

    location = pick(options, title, indicator='->')[0]
    return location


# yay it works
def add_favorites():
    with open('example.csv') as csv_file:
        parsed_csv = csv.reader(csv_file)
        options = next(parsed_csv)
        options[-1] = options[-1].replace(';', '')
    places_to_add = pick(options, "What do you want to add", multiselect=True)
    print(places_to_add)
    final_places_to_add = []
    for place in places_to_add:
        final_places_to_add.append(place[0])
    with open('favorites.csv', mode='w') as csv_file:
        favorite_changer = csv.writer(csv_file, delimiter=',')
        favorite_changer.writerow(final_places_to_add)




def edit_favorites(filename, options_another):
    title = "Marca tus destinos favoritos (ESPACIO para marcar, ENTER para confirmar):"
    primera_vez = input("Primera vez? [Y/n]  ")
    if primera_vez == "Y":
        options = create_options_list(filename)
    else:
        options = options_another
    selected = pick(options, title, multiselect=True, min_selection_count=0)
    new_list = []
    for option in selected:  # implement later with map()
        new_list.append(option[0])
    return new_list


def change_favorites(list):
    with open("favorites.csv", mode="w") as csv_file:
        favorite_changer = csv.writer(csv_file, delimiter=',')
        favorite_changer.writerow(list) 

def read_favorites():
    with open("favorites.csv", mode="r") as csv_file:
        favorite_reader = csv.reader(csv_file, delimiter=",")
        options = next(favorite_reader)
    return options


def create_options_list(filename):
    with open(filename) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
        first_row[-1] = first_row[-1].replace(';', '')
    return first_row





def print_directions(directions):
    # pendiente:
    for place in directions:
        print("Ve al nodo", place)


def __init__():
    filename = "example.csv"
    welcome_user()
    the_list = edit_favorites(filename, read_favorites)
    change_favorites(the_list)
    # This itself could be a function
    options = create_options_list(filename, read_favorites(filename))
    initial_location = pick_locations(options, True)
    options.remove(initial_location)
    final_location = pick_locations(options, False)
    print(f'''\nThe user is at {initial_location} and is going to {final_location}\n''')


# __init__()

add_favorites()