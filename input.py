from pick import pick


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
