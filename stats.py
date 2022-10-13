import json


stats_path = 'time_and_distance.json'


def get_json_as_dict() -> dict:
    # TODO Use path instead of string
    with open(stats_path) as file:
        return json.load(file)

def get_json_as_tuple() -> tuple:
    stats = get_json_as_dict()
    return stats['distance'], stats['time']


def save_dict_as_json(json_object: dict) -> None:
    # TODO Use path instead of string
    with open(stats_path, mode='w') as file:
        json.dump(json_object, file,
                  indent=2)  # Prettify json


def sum_new_stats(steps: int, walking_time: int) -> dict:
    stats = get_json_as_dict()
    stats['distance'] += steps
    stats['time'] += walking_time
    return stats


def update_stats(steps: int, walking_time: int) -> None:
    # This seems redundant, but I find it better to decompose
    new_stats = sum_new_stats(steps, walking_time)
    save_dict_as_json(new_stats)


# TODO Move to setup module
def _reset_stats() -> None:
    # NOTE: The program should never run this
    if input('Reset stats?!!! [Y/n] ') == 'Y':
        stats = get_json_as_dict()
        stats['time'] = 0
        stats['distance'] = 0
        save_dict_as_json(stats)
