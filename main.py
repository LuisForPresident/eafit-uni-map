from pick import pick

import dijkstra
import favorites
import input
import results
from options import create_options
import start

# TODO Write the paths in a global and better way
# Declare global paths for csv files
graph_path = 'example.csv'
favorites_path = 'favorites.csv'
time_and_distance_path = 'time_and_distance.csv'


# TODO Learn what __main__() and __init__() mean

def main():
    if start.travel() is True:
        # Get the location
        location_options = create_options()
        location = input.get_location(location_options)

        # Get the destination
        from_favorites = favorites.choose_from_favorites()
        if from_favorites is True:
            destination_options = favorites.create_favorites_list()
        else:
            destination_options = location_options
        destination = input.get_destination(destination_options, location)

        # Calculate the shortest path
        directions, distance = dijkstra.get_shortest_path_and_distance(location, destination)

        # Print the list of directions
        decision = results.show_directions(directions, distance)
        if decision is True:
            main()
        else:
            exit()
    else:
        options = []

        all_places = create_options()
        if favorites.is_there_at_least_one_not_favorite(all_places):
            options.append('Add')
        if favorites.is_there_at_least_one_favorite():
            options.append('Remove')
        # options.append('Add') if is_there_at_least_one_not_favorite() else None
        # options.append('Remove') if is_there_at_least_one_favorite() else None

        title = 'Edit favorites:'
        decision = pick(options, title)[0]  # In this case, get the text
        if decision == 'Add':
            favorites.add_favorites(all_places)
        else:
            favorites.remove_favorites()
        main()

        # selected = pick(options, title, multiselect=True, min_selection_count=0)
        # new_list = []
        # for option in selected:  # implement later with map()
        #     new_list.append(option[0])
        # return new_list


if __name__ == '__main__':
    main()
