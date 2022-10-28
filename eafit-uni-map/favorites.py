import csv

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




def add_favorites(all_places: list):
    with open(config.FAVORITES_PATH, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            already_favorites = []

    for favorite in already_favorites:
        if favorite in all_places:
            all_places.remove(favorite)

    try:
        favorites_from_pick = pick(all_places,
                                   'Select one or more with SPACE and confirm with ENTER',
                                   multiselect=True,
                                   min_selection_count=1)
    finally:
        favorites_to_add = []
        for favorite in favorites_from_pick:
            favorites_to_add.append(favorite[0])

        # so it doesn't overwrite the existing favorites
        favorites_to_add.extend(already_favorites)
        favorites_to_add.sort()

        with open(config.FAVORITES_PATH, mode='w') as final_favorites:
            csv.writer(final_favorites, delimiter=',').writerow(favorites_to_add)


def remove_favorites():
    with open(config.FAVORITES_PATH, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            already_favorites = []
    try:
        favorites_from_pick = pick(already_favorites,
                                   'Select one or more with SPACE and confirm with ENTER',
                                   multiselect=True,
                                   min_selection_count=1)
    finally:
        # extract the A,B,C values (etc.) from the list of tuples
        favorites_to_remove = []
        for favorite in favorites_from_pick:
            favorites_to_remove.append(favorite[0])
        # favorites_to_remove = list(list(zip(*favorites_from_pick))[0])

        for favorite in favorites_to_remove:
            if favorite in already_favorites:
                already_favorites.remove(favorite)
        already_favorites.sort()
        with open(config.FAVORITES_PATH, mode='w') as final_favorites:
            csv.writer(final_favorites, delimiter=',').writerow(already_favorites)


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
