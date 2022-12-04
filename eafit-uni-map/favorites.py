"""
Add and remove places as favorites.
"""

from json import load, dump

from pick import pick, Option

import config


def retrieve_favorites() -> list:
    """Returns the list of favorites."""
    with open(config.FAVORITES_PATH, mode="r", encoding="utf-8") as file:
        return load(file)


def store_favorites(new_favorites: list) -> None:
    """Updates the favorites file."""
    with open(config.FAVORITES_PATH, mode="w", encoding="utf-8") as file:
        dump(new_favorites, file, indent=2)


def add_favorites(all_places: list) -> None:
    """Adds favorites to list."""
    current_favorites = retrieve_favorites()
    favorites_to_add = pick(
        list(set(all_places) - set(current_favorites)),
        "SPACE to select one or more\nENTER to add",
        multiselect=True,
        min_selection_count=1,
    )
    favorites_to_add = [text for text, index in favorites_to_add]
    updated_favorites = list(set(current_favorites) ^ set(favorites_to_add))
    store_favorites(updated_favorites)


def remove_favorites() -> None:
    """Removes favorites from list."""
    current_favorites = retrieve_favorites()
    favorites_to_remove = pick(
        current_favorites,
        "SPACE to select one or more\nENTER to remove",
        multiselect=True,
        min_selection_count=1,
    )
    favorites_to_remove = [text for text, index in favorites_to_remove]
    updated_favorites = list(set(current_favorites) - set(favorites_to_remove))
    store_favorites(updated_favorites)


def can_remove_favorites() -> bool:
    """Returns True if there are favorites."""
    current_favorites = retrieve_favorites()
    return bool(current_favorites)


def can_add_favorites(all_places: list) -> bool:
    """Returns True if not favorites exist."""
    current_favorites = retrieve_favorites()
    unfavorited_places = list(set(all_places) - set(current_favorites))
    return bool(unfavorited_places)  # True if there are unfavorites


def should_add_favorites(possible_actions: list, all_places: list) -> None:
    """Prompts user for editing operation (add, remove) or backtrack."""
    # -1 since choice.value expects an Option with value
    possible_actions.append(Option("Go back", -1))
    title = "Pick an option (or go back)"

    choice, _ = pick(possible_actions, title)
    user_wants_to_add_favorites = choice.value

    if user_wants_to_add_favorites is True:
        add_favorites(all_places)
    elif user_wants_to_add_favorites is False:
        remove_favorites()
    else:
        # Abort editing
        pass
