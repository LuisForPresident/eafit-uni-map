import favorites
import results
import choice
import stats

import config

import networkx as nx
from pick import Option


def main():
    # Create graph from edgelist file
    Graph = nx.read_weighted_edgelist(
        config.graph_path,
        comments='#',
        delimiter=','  # csv-like
    )

    # Get all-time stats
    current_stats = stats.get_formatted_stats()

    # Pass stats to main menu function
    if choice.select_travel(current_stats) is True:

        # Choose location
        location_options = list(Graph.nodes)
        location = choice.get_location(location_options)

        # Choose destination from: All options or favorites?
        from_favorites = favorites.choose_from_favorites()
        if from_favorites is True:
            destination_options = favorites.create_favorites_list()
        else:
            destination_options = location_options

        # Choose destination
        destination = choice.get_destination(destination_options, location)

        # Compute the shortest path
        directions = nx.dijkstra_path(Graph, location, destination)

        # Get length of that shortest path
        distance_in_meters = nx.dijkstra_path_length(Graph, location, destination)

        # Calculate steps and walking time
        steps = results.convert_meters_to_steps(distance_in_meters)
        walking_time = results.estimate_walking_time(distance_in_meters)
        
        # Add trip stats to all-time stats
        stats.update_stats(steps, walking_time)

        # Display directions and stats for that trip
        stats_str = results.get_formatted_stats(steps, walking_time)
        start_again = results.show_directions(directions, stats_str)

        # Q: Go back to start menu or quit program?
        if start_again is True:
            main()
        else:
            exit()
    else:
        possible_actions = []

        all_places = list(Graph.nodes)
        if favorites.is_there_at_least_one_not_favorite(all_places):
            possible_actions.append(Option('Add', True))
        if favorites.is_there_at_least_one_favorite():
            possible_actions.append(Option('Remove', False))

        # Q: Add or remove favorites?
        favorites.should_add_favorites(possible_actions, all_places)

        # Go back to start menu
        main()


if __name__ == '__main__':
    main()
