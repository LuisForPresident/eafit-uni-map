from pick import pick, Option

import csv

graph_path = 'example.csv'


def create_options() -> list:
    with open(graph_path) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
    return first_row


def select_travel(stats: tuple) -> bool:
    options = [
        Option('Travel', True),
        Option('Edit favorites', False)
    ]
    title = get_start_title(stats)
    decision, index = pick(options, title, indicator='->')
    # decision is an Option object
    # Implemented here:
    # https://github.com/wong2/pick/commit/a043d6699f40818c0482e09a1f2fe3952d2e8c40
    return decision.value  # Either 'True' or 'False'


def get_start_title(stats: tuple) -> str:
    distance, time = stats
    stats_to_display = 'You have walked {0} steps in {1} secs'.format(str(distance), str(time))
    start_title = 'EAFIT University Map - 2022'
    authors = 'Luis M. Torres-Villegas & Miguel Suárez-Obando'
    repository_url = 'https://github.com/LuisForPresident/eafit-uni-map/'
    welcome_message = 'Welcome! Get directions based on some landmarks on campus.'
    # TODO Format the return without concatenating with plus signs
    return '\n' + start_title + '\n' + authors + '\n' + repository_url + '\n\n' + welcome_message + '\n\n' + stats_to_display
