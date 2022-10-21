from pick import pick, Option

import csv

import config


def create_options() -> list:
    with open(config.graph_path) as csv_file:
        parsed_csv = csv.reader(csv_file)
        first_row = next(parsed_csv)
    return first_row


def get_location(options: list) -> str:
    title = 'Select your current location:'
    location, index = pick(options, title, indicator='->')
    return location


def get_destination(options: list, location: str) -> str:
    # Remove location from the available options
    if location in options:  # For the favorites special case
        options.remove(location)  # Destination must not be the location
    options.sort()
    title = 'Select your destination:'
    destination, index = pick(options, title, indicator='->')
    return destination


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
