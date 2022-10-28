import json
from pick import pick, Option

import config


def choose_from_favorites() -> bool:
    options = [
        Option('All options', False),
    ]
    if is_there_at_least_one_favorite() is True:
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


def is_there_at_least_one_favorite():
    with open(config.FAVORITES_PATH, mode='r') as favorites:
        try:
            if next(csv.reader(favorites, delimiter=',')):
                return True
            else:
                return False
        except StopIteration:
            return False


def is_there_at_least_one_not_favorite(all_places: list):
    with open(config.FAVORITES_PATH, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            return True

    for favorite in already_favorites:
        if favorite in all_places:
            all_places.remove(favorite)
    if len(all_places) == 0:
        return False
    else:
        return True


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
