import json


def get_json_as_dict(stats_path: str) -> dict:
    # TODO Use path instead of string
    with open(stats_path) as file:
        return json.load(file)


def get_json_as_tuple(stats_path: str) -> tuple:
    stats = get_json_as_dict(stats_path)
    return stats['distance'], stats['time']


def save_dict_as_json(json_object: dict, stats_path: str) -> None:
    # TODO Use path instead of string
    with open(stats_path, mode='w') as file:
        json.dump(json_object, file,
                  indent=2)  # Prettify json


def sum_new_stats(steps: int, walking_time: int, stats_path: str) -> dict:
    stats = get_json_as_dict(stats_path)
    stats['distance'] += steps
    stats['time'] += walking_time
    return stats


def update_stats(steps: int, walking_time: int) -> None:
    # This seems redundant, but I find it better to decompose
    new_stats = sum_new_stats(steps, walking_time)
    save_dict_as_json(new_stats)


# TODO Move to setup module
def _reset_stats(stats_path: str) -> None:
    # NOTE: The program should never run this
    if input('Reset stats?!!! [Y/n] ') == 'Y':
        stats = get_json_as_dict(stats_path)
        stats['time'] = 0
        stats['distance'] = 0
        save_dict_as_json(stats)
