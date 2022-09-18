from pick import *
from dijkstra import *  # for the main algorithm
import csv

def welcome_user():
    print("\nEAFIT University Map - 2022\nLuis M. Torres-Villegas & Miguel Suárez-Obando\nhttps://github.com/LuisForPresident/eafit-uni-map/\n")
    print("Welcome! Get directions based on some landmarks on campus.")

    # name : string = input("What's your name: ")
    # print(f"Hello, {name}!")


# pending
def create_options():
    with open("example.csv") as csv_file:
        parsed_csv = csv.reader(csv_file, delimiter=";", line_num = 0)
    print(parsed_csv)


def pick_initial_location():
    title = "Where are you now (that I need you)?: "
    options = ['Bloque 18', 'Bloque 29', 'Biblioteca', 'Cafetería']
    option, index = pick(options, title)
    print(option, index)


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
    welcome_user()
    pick_initial_location()
    initial_location = get_initial_location()
    # print(f"\nThe user is at {initial_location} and is going to {final_location}\n")

    if (initial_location == final_location):
        exit()
    else:
        print_directions(get_shortest_path(initial_location, final_location))
    


__init__()
