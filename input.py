from pick import pick


def get_location(options: list) -> str:
    title = 'Select your current location:'
    location = pick(options, title, indicator='->')[0]
    return location


def get_destination(options: list, location: str) -> str:
    # Remove location from the available options
    if location in options:  # For the favorites special case
        options.remove(location)  # Destination must not be the location
    options.sort()
    title = 'Select your destination:'
    destination = pick(options, title, indicator='->')[0]
    return destination
