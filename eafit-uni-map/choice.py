"""
Functions that prompt user for input
from a selection using the `pick` module.
"""

from pick import pick, Option


def get_location(options: list) -> str:
    """Prompts user for location."""
    options.sort()
    title = "Select your current location:"
    location, index = pick(options, title, indicator="->")
    return location


def get_destination(options: list, location: str) -> str:
    """Prompts user for destination."""
    # Remove location from the available options
    if location in options:  # For the favorites special case
        options.remove(location)  # Destination must not be the location
    options.sort()
    title = "Select your destination:"
    destination, index = pick(options, title, indicator="->")
    return destination


def select_travel(stats: tuple) -> bool:
    """Prompts user: 1) get directions or 2) edit favorites."""
    options = [Option("Travel", True), Option("Edit favorites", False)]
    title = get_start_title(stats)
    decision, index = pick(options, title, indicator="->")
    return decision.value  # Either 'True' or 'False'


def get_start_title(stats: str) -> str:
    """Returns the title displayed at start."""
    stats_to_display = f"You have walked {stats}"
    start_title = "EAFIT University Map - 2022"
    authors = "Luis M. Torres-Villegas & Miguel Suárez-Obando"
    repository_url = "https://github.com/LuisForPresident/eafit-uni-map/"
    welcome_message = "Welcome! Get directions based on some landmarks on campus."
    return f"\n{start_title}\n{authors}\n{repository_url}\n\n{welcome_message}\n\n{stats_to_display}"
