import csv

graph_path = 'example.csv'


def create_options() -> list:
    with open(graph_path) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
        first_row[-1] = first_row[-1].replace(';', '')
    return first_row
