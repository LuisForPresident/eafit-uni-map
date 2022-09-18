from dijkstra import *  # for the main algorithm

def welcome_user():
    print("\nEAFIT University Map - 2022\nLuis M. Torres-Villegas & Miguel Suárez-Obando\nhttps://github.com/LuisForPresident/eafit-uni-map/\n")
    print("Welcome! Get directions based on some landmarks on campus.")

    # name : string = input("What's your name: ")
    # print(f"Hello, {name}!")


def get_initial_and_final_locations():
    # this should be decomposed into two functions
    return input("\nWhere are you?  ").upper(), input("Where do you want to go?  ").upper()


def print_directions(directions):
    for place in directions:
        print("Ve al nodo", place)


def __init__():
    welcome_user()
    initial_location, final_location = get_initial_and_final_locations()
    # print(f"\nThe user is at {initial_location} and is going to {final_location}\n")

    print_directions(get_shortest_path(initial_location, final_location))
    


__init__()
