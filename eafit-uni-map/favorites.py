import json
from pick import pick, Option

import config


def choose_from_favorites() -> bool:
    options = [
        Option('All options', False),
    ]
    if can_remove_favorites() is True:
        options.append(Option('Favorites', True))
    title = 'Choose destination from:'
    decision, index = pick(options, title, indicator='->')
    return decision.value


def retrieve_favorites() -> list:
    with open(config.FAVORITES_PATH, mode='r') as file:
        return json.load(file)

def store_favorites(new_favorites: list) -> None:
    with open(config.FAVORITES_PATH, mode='w') as file:
        json.dump(new_favorites, file, indent=2)


def add_favorites(all_places: list) -> None:
    current_favorites = retrieve_favorites()
    favorites_to_add = pick(list(set(all_places) - set(current_favorites)),
                            'SPACE to select one or more\nENTER to add',
                            multiselect=True,
                            min_selection_count=1)
    favorites_to_add = [text for text, index in favorites_to_add]
    updated_favorites = list(set(current_favorites) ^ set(favorites_to_add))
    store_favorites(updated_favorites)


def remove_favorites() -> None:
    current_favorites = retrieve_favorites()
    favorites_to_remove = pick(current_favorites,
                               'SPACE to select one or more\nENTER to remove',
                               multiselect=True,
                               min_selection_count=1)
    favorites_to_remove = [text for text, index in favorites_to_remove]
    updated_favorites = list(set(current_favorites) - set(favorites_to_remove))
    store_favorites(updated_favorites)


def can_remove_favorites() -> bool:
    current_favorites = retrieve_favorites()
    if current_favorites:  # if list is not empty
        return True
    else:
        return False


def can_add_favorites(all_places: list) -> bool:
    current_favorites = retrieve_favorites()
    if list(set(all_places) - set(current_favorites)):  # if list is not empty
        return True
    else:
        return False


def should_add_favorites(possible_actions: list, all_places: list) -> None:
    # -1 since choice.value expects an Option with value
    possible_actions.append(Option('Go back', -1))
    title = 'Pick an option (or go back)'

    choice, index = pick(possible_actions, title)
    user_wants_to_add_favorites = choice.value

    if user_wants_to_add_favorites is True:
        add_favorites(all_places)
    elif user_wants_to_add_favorites is False:
        remove_favorites()
    else:
        # Abort editing
        pass
