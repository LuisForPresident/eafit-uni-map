from pick import pick


def travel():
    options = ['Travel', 'Edit favorites']
    title = '\nEAFIT University Map - 2022\n' \
            'Luis M. Torres-Villegas & Miguel Suárez-Obando\n' \
            'https://github.com/LuisForPresident/eafit-uni-map/\n\n' \
            'Welcome! Get directions based on some landmarks on campus.'
    decision = pick(options, title, indicator='->')[1]  # Get the index
    return bool(decision == 0)
    # if decision == 0:  # 'Travel'
    #     return True
    # else:
    #     return False  # 'Edit favorites'
    # https://docs.python.org/3/library/functions.html#bool
