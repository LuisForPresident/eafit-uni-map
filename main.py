from pick import pick

import dijkstra
import favorites
import results
import choice
import stats

# TODO Write the paths in a global and better way
# Declare global paths for csv files
graph_path = 'example.csv'
favorites_path = 'favorites.csv'
stats_path = 'time_and_distance.json'


# TODO Learn what __main__() and __init__() mean

def main():
    # Get stats and send them to start menu
    current_stats = stats.get_json_as_tuple(stats_path)

    if choice.select_travel(current_stats) is True:
        # Get the location
        location_options = choice.create_options(graph_path)
        location = choice.get_location(location_options)

        # Get the destination
        from_favorites = favorites.choose_from_favorites()
        if from_favorites is True:
            destination_options = favorites.create_favorites_list()
        else:
            destination_options = location_options
        destination = choice.get_destination(destination_options, location)

        # Compute the shortest path
        directions, distance = dijkstra.get_shortest_path_and_distance(location, destination, graph_path)

        # Display the list of directions and stats
        start_again = results.show_directions(directions, distance)

        # Store stats from this trip
        steps = results.convert_to_steps(distance)
        walking_time = results.estimate_walking_time(distance)
        stats.update_stats(steps, walking_time)

        # Go back to start menu or quit program
        if start_again is True:
            main()
        else:
            exit()
    else:
        possible_actions = []

        all_places = choice.create_options(graph_path)
        if favorites.is_there_at_least_one_not_favorite(all_places):
            possible_actions.append('Add')
        if favorites.is_there_at_least_one_favorite():
            possible_actions.append('Remove')

        favorites.which_favorites_action(possible_actions, all_places)

        main()


if __name__ == '__main__':
    main()
