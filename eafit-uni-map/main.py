"""
The program itself.
"""

import favorites
import results
import stats

import config

from networkx import read_weighted_edgelist, dijkstra_path, dijkstra_path_length
from pick import Option, pick


def main():
    """Runs the program itself."""
    # Initialize the campus graph from the .edgelist file
    Graph = read_weighted_edgelist(config.GRAPH_PATH, delimiter=";")

    # Get all-time stats to show at start menu
    current_stats = stats.get_formatted_stats()

    start_menu_title = """
EAFIT University Map - 2022
Luis M. Torres-Villegas & Miguel Suárez-Obando
https://github.com/LuisForPresident/eafit-uni-map/

Welcome! Get directions based on some landmarks on campus.

You have walked {stats}"""

    # Prompt the user to either get directions or edit the list of favorites
    should_get_directions, _ = pick(
        [Option("Travel", True), Option("Edit favorites", False)],
        start_menu_title.format(stats=current_stats),
        indicator="->",
    )

    if should_get_directions.value is True:

        # Prompt the user to select the location
        location_places = list(Graph.nodes)
        location, _ = pick(
            sorted(location_places), "Select your current location:", indicator="->"
        )

        # Show the destinations from all options or just the favorite places?
        destination_places: list
        choose_from = [Option("All options", False)]
        if favorites.can_remove_favorites() is True:
            choose_from.append(Option("Favorites", True))
        from_favorites, _ = pick(
            choose_from, "Choose destination from:", indicator="->"
        )

        # Use the appropiate list of places
        if from_favorites.value is True:
            destination_places = favorites.retrieve_favorites()
        else:
            destination_places = location_places

        # Prompt the user to select the destination
        if location in destination_places:
            destination_places.remove(location)
        destination, _ = pick(
            sorted(destination_places), "Select your destination:", indicator="->"
        )

        # Compute the shortest path using Dijkstra's algorithm
        shortest_path = dijkstra_path(Graph, location, destination)
        distance_in_meters = dijkstra_path_length(Graph, location, destination)

        # Calculate the stats for that trip
        steps = results.convert_meters_to_steps(distance_in_meters)
        walking_time = results.estimate_walking_time(distance_in_meters)

        # Add trip stats to all-time stats
        stats.update_stats(steps, walking_time)

        trip_stats = stats.get_formatted_stats(steps, walking_time)
        go_back_to_main_menu = results.show_directions(shortest_path, trip_stats)

        if go_back_to_main_menu is True:
            main()
        else:
            exit()
    else:
        available_editing_operations = []

        all_places = list(Graph.nodes)
        if favorites.can_add_favorites(all_places):
            available_editing_operations.append(Option("Add new places", True))
        if favorites.can_remove_favorites():
            available_editing_operations.append(Option("Remove existing places", False))

        # Q: Add or remove favorites?
        favorites.should_add_favorites(available_editing_operations, all_places)

        # Go back to start menu
        main()


if __name__ == "__main__":
    main()
