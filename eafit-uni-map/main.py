import dijkstra
import favorites
import results
import choice
import stats

import config

import networkx as nx


def main():
    # Get all-time stats
    current_stats = stats.get_json_as_tuple()

    # Pass stats to main menu function
    if choice.select_travel(current_stats) is True:
        # Create graph from edgelist file
        Graph = nx.read_weighted_edgelist(
            config.graph_path,
            comments='#',
            delimiter=','  # csv-like
        )

        # Choose location
        location_options = choice.create_options()
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
        directions, distance = dijkstra.get_shortest_path_and_distance(location, destination)

        # Display directions and stats for that trip
        start_again = results.show_directions(directions, distance)

        # TODO Pass data directly to show_directions()
        # Calculate steps and walking time
        steps = results.convert_to_steps(distance)
        walking_time = results.estimate_walking_time(distance)

        # Add trip stats to all-time stats
        stats.update_stats(steps, walking_time)

        # Q: Go back to start menu or quit program?
        if start_again is True:
            main()
        else:
            exit()
    else:
        possible_actions = []

        all_places = choice.create_options()
        if favorites.is_there_at_least_one_not_favorite(all_places):
            possible_actions.append('Add')
        if favorites.is_there_at_least_one_favorite():
            possible_actions.append('Remove')

        # Q: Add or remove favorites?
        favorites.which_favorites_action(possible_actions, all_places)

        # Go back to start menu
        main()


if __name__ == '__main__':
    main()
