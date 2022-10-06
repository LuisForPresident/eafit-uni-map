import heapq  # https://docs.python.org/3/library/heapq.html
import csv  # https://docs.python.org/3/library/csv.html
from collections import deque
# https://docs.python.org/3/library/collections.html?highlight=deque#deque-objects


# Return input csv file of edge list as an array
def parse_csv_input(file_name):
    edge_list = []

    with open(file_name) as csv_file:
        parsed_csv = csv.reader(csv_file, delimiter=";")
        for edge in parsed_csv:
            edge_list.append(edge[0].split(","))

    return edge_list


# Return graph dictionary with placeholder keys
def initialize_graph_keys(edge_list):
    graph_dict = {}

    for edge in edge_list:
        if edge not in graph_dict:
            graph_dict[edge] = []

    return graph_dict


# Return graph dictionary with weighted edges
def add_graph_edges(graph_dict, initial_node, final_node, distance):
    graph_dict[initial_node].append((distance, final_node))
    return graph_dict


# Return distances from initial_node to every other node
# found with Dijkstra's algorithm as a dictionary
def calculate_edge_distances(graph_dict, initial_node):
    least_distance_nodes = []
    distance = {edge: 'infinity' for edge in graph_dict.keys()}
    path = {}

    heapq.heappush(least_distance_nodes, (0, initial_node))  # Priority queue
    while least_distance_nodes:
        current_weight, current_node = heapq.heappop(least_distance_nodes)
            distance[current_node] = current_weight
            for (weight, node) in graph_dict[current_node]:
                heapq.heappush(least_distance_nodes,
                               (current_weight+weight, node))
                if (node not in path) or (current_weight+weight
                                          < path[node][1]):
                    path[node] = (current_node, weight)

    return distance, path


# Return directions as a deque
def show_path(path, initial_node, final_node):
    directions = deque()
    directions.append(final_node)
    search = path[final_node][0]  # Avoids conversion to deque from splitting str into a list

    while search in path:
        directions.appendleft(search)
        search = path[search][0]
    directions.appendleft(initial_node)
    return directions


    edge_list = parse_csv_input(file_name)
    graph = initialize_graph_keys(edge_list[0])
    for edge in edge_list[1:]:
        add_graph_edges(graph, edge[0], edge[1], float(edge[2]))

    distance_dict = calculate_edge_distances(graph, initial_node)
    distance = int(distance_dict[0][final_node])
    path = distance_dict[1]
    if final_node in path:
        deque_directions = show_path(path, initial_node, final_node)
    return deque_directions, distance
