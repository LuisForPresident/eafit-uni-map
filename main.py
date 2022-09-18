import csv
from pick import *
from dijkstra import *


def welcome_user():
    print("\nEAFIT University Map - 2022\nLuis M. Torres-Villegas & Miguel Suárez-Obando\nhttps://github.com/LuisForPresident/eafit-uni-map/\n")
    print("Welcome! Get directions based on some landmarks on campus.")


def create_options_list(filename):
    with open(filename) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
        first_row[-1] = first_row[-1].replace(';', '')
    return first_row


def pick_locations(options, first):
    if first == True:
        title = "Where are you now?"
    else:
        title = "Where are you going?"

    location = pick(options, title, indicator='->')[0]
    return location


def get_initial_location():
    return input("\nWhere are you?  ").upper()
    # pendiente: excepcion de si no esta en la lista


def get_final_location():
    # pendiente: excepcion de si no esta en la lista
    return input("Where do you want to go?  ").upper()


def print_directions(directions):
    # pendiente: 
    for place in directions:
        print("Ve al nodo", place)


def __init__():
    filename = "example.csv"
    welcome_user()
    start_message = input("Are you kind of cool? [Y/n] ")  # will delete later, it's just so that the user sees the welcome message

    # This itself could be a function
    options = create_options_list(filename)
    initial_location = pick_locations(options, True)
    options.remove(initial_location)
    final_location = pick_locations(options, False)
    print(f"\nThe user is at {initial_location} and is going to {final_location}\n")


__init__()
