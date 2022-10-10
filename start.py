from pick import pick, Option


def select_travel() -> bool:
    options = [
        Option('Travel', True),
        Option('Edit favorites', False)
    ]
    title = get_start_title()
    decision, index = pick(options, title, indicator='->')
    # decision is an Option object
    # Implemented here:
    # https://github.com/wong2/pick/commit/a043d6699f40818c0482e09a1f2fe3952d2e8c40
    return decision.value  # Either 'True' or 'False'


def get_start_title() -> str:
    start_title = 'EAFIT University Map - 2022'
    authors = 'Luis M. Torres-Villegas & Miguel Suárez-Obando'
    repository_url = 'https://github.com/LuisForPresident/eafit-uni-map/'
    welcome_message = 'Welcome! Get directions based on some landmarks on campus.'
    # TODO Format the return without concatenating with plus signs
    return '\n' + start_title + '\n' + authors + '\n' + repository_url + '\n\n' + welcome_message
