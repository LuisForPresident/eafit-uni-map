import dijkstra
import favorites
import input
import options
import results
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
        location_options = options.create_options()
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
        decision = results.print_directions(directions, distance)
        if decision == 0:
            main()
        else:
            exit()
    else:
        favorites.edit_favorites()


if __name__ == '__main__':
    main()
