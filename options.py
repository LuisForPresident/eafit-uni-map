import csv

graph_path = 'example.csv'


def create_options() -> list:
    with open(graph_path) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
    return first_row
