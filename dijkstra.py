import heapq
import csv
from collections import deque
from typing import Any

graph_path = 'example.csv'
favorites_path = 'favorites.csv'
time_and_distance_path = 'time_and_distance.csv'


# Return input csv file of edge list as a list
def parse_csv_input(file_name: str):
    edge_list = []
    with open(file_name) as csv_file:
        parsed_csv = csv.reader(csv_file, delimiter='\n')
        for edge in parsed_csv:
            edge_list.append(edge[0].split(','))
    return edge_list


# Return graph dictionary with placeholder keys
def initialize_graph_keys(edge_list: list):
    graph_dict = {}
    for edge in edge_list:
        if edge not in graph_dict:
            graph_dict[edge] = []
    return graph_dict


# Return graph dictionary with weighted edges
def add_graph_edges(graph_dict: dict,
                    initial_node: str,
                    final_node: str,
                    distance: float):
    graph_dict[initial_node].append((distance, final_node))
    return graph_dict


# Return distances from initial_node to every other node
# found with Dijkstra's algorithm as a dictionary
def calculate_edge_distances(graph_dict: dict, initial_node: str):
    least_distance_nodes = []
    distance = {edge: 'infinity' for edge in graph_dict.keys()}
    path = {}
    heapq.heappush(least_distance_nodes, (0, initial_node))  # Priority queue
    while least_distance_nodes:
        current_weight, current_node = heapq.heappop(least_distance_nodes)
        if distance[current_node] == 'infinity':
            distance[current_node] = current_weight
            for (weight, node) in graph_dict[current_node]:
                heapq.heappush(least_distance_nodes,
                               (current_weight + weight, node))
                if (node not in path) or (current_weight + weight
                                          < path[node][1]):
                    path[node] = (current_node, weight)
    return distance, path


# Return directions as a deque
def show_path(path: dict, initial_node: str, final_node: str):
    directions = deque()
    # Avoid conversion to deque from splitting str into a list
    directions.append(final_node)
    search = path[final_node][0]
    while search in path:
        directions.appendleft(search)
        search = path[search][0]
    directions.appendleft(initial_node)
    return directions


def get_shortest_path_and_distance(initial_node: str, final_node: str):
    # Weird special case I really do not want :/
    special_case = check_special_case(initial_node, final_node)
    if special_case is True:
        # initial_node, final_node = final_node, initial_node
        swap_temp_var = final_node
        final_node = initial_node
        initial_node = swap_temp_var

    deque_directions = deque()
    edge_list = parse_csv_input(graph_path)
    graph = initialize_graph_keys(edge_list[0])
    for edge in edge_list[1:]:
        add_graph_edges(graph, edge[0], edge[1], float(edge[2]))
    distance_dict = calculate_edge_distances(graph, initial_node)
    distance = int(distance_dict[0][final_node])
    path = distance_dict[1]
    if final_node in path:
        deque_directions: deque[Any] = show_path(path,
                                                 initial_node,
                                                 final_node)
    if special_case is True:
        deque_directions.reverse()
    return deque_directions, distance


def check_special_case(initial_node, final_node) -> bool:
    # See issue #36 on GitHub
    # Equivalent to options.create_options()
    nodes = parse_csv_input(graph_path)[0]
    final_index = nodes.index(final_node)
    initial_index = nodes.index(initial_node)
    if final_index < initial_index:
        return True
    else:
        return False
