import csv

from pick import pick

favorites_path = 'favorites.csv'


def choose_from_favorites():
    options = ['All options', 'Favorites']
    title = 'Choose destination from:'
    decision = pick(options, title, indicator='->')[1]  # Get the index
    if decision != 0:
        return True
    else:
        return False


def create_favorites_list():
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
            return already_favorites
        except StopIteration:
            choose_from_favorites()


def add_favorites():
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            already_favorites = []
    all_places = create_options_list()

    for favorite in already_favorites:
        if favorite in all_places:
            all_places.remove(favorite)

    try:
        favorites_from_pick = pick(all_places, 'Select favorites to add with SPACE', multiselect=True,
                                   min_selection_count=1)
    except ValueError:
        choose_at_start_menu()
        # TODO maybe the function itself should not be available if this error occurs?
    else:
        favorites_to_add = []
        for favorite in favorites_from_pick:
            favorites_to_add.append(favorite[0])
        favorites_to_add.extend(already_favorites)  # so it doesn't overwrite the existing favorites
        favorites_to_add.sort()

        with open(favorites_path, mode='w') as final_favorites:
            csv.writer(final_favorites, delimiter=',').writerow(favorites_to_add)


def remove_favorites():
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            already_favorites = []
    try:
        favorites_from_pick = pick(already_favorites, 'Select favorites to remove with SPACE', multiselect=True,
                                   min_selection_count=1)
    except ValueError:
        choose_at_start_menu()
        # TODO maybe the function itself should not be available if this error occurs?
    else:
        # extract the A,B,C values (etc.) from the list of tuples
        # BUG
        favorites_to_remove = []
        for favorite in favorites_from_pick:
            favorites_to_remove.append(favorite[0])
        # favorites_to_remove = list(list(zip(*favorites_from_pick))[0])
        print(favorites_to_remove)

        for favorite in favorites_to_remove:
            if favorite in already_favorites:
                already_favorites.remove(favorite)
        already_favorites.sort()
        with open(favorites_path, mode='w') as final_favorites:
            csv.writer(final_favorites, delimiter=',').writerow(already_favorites)


def is_there_at_least_one_favorite():
    with open(favorites_path, mode='r') as favorites:
        try:
            if next(csv.reader(favorites, delimiter=',')):
                return True
            else:
                return False
        except StopIteration:
            return False


def is_there_at_least_one_not_favorite():
    with open(favorites_path, mode='r') as favorites:
        try:
            already_favorites = next(csv.reader(favorites, delimiter=','))
        except StopIteration:
            return True
    all_places = create_options_list()
    for favorite in already_favorites:
        if favorite in all_places:
            all_places.remove(favorite)
    if len(all_places) == 0:
        return False
    else:
        return True


def change_favorites(options):
    with open('favorites.csv', mode='write') as csv_file:
        favorite_changer = csv.writer(csv_file, delimiter=',')
        favorite_changer.writerow(options)


# TODO Refactor the read favorites code
def read_favorites(favorites_path):
    with open(favorites_path, mode='read') as csv_file:
        favorite_reader = csv.reader(csv_file, delimiter=',')
        options = next(favorite_reader)
    return options


def edit_favorites():
    options = []

    if is_there_at_least_one_not_favorite():
        options.append('Add')
    if is_there_at_least_one_favorite():
        options.append('Remove')
    # options.append('Add') if is_there_at_least_one_not_favorite() else None
    # options.append('Remove') if is_there_at_least_one_favorite() else None

    title = 'Edit favorites:'
    decision = pick(options, title)[0]  # In this case, get the text
    if decision == 'Add':
        add_favorites()
    else:
        remove_favorites()
    procedure()

    # selected = pick(options, title, multiselect=True, min_selection_count=0)
    # new_list = []
    # for option in selected:  # implement later with map()
    #     new_list.append(option[0])
    # return new_list
