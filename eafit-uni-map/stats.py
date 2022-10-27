import json

import config


def get_stats_dict() -> dict:
    with open(config.STATS_PATH) as file:
        return json.load(file)


def get_formatted_stats() -> str:
    current_stats = get_stats_dict()

    distance = str(current_stats['distance'])
    timespan: int = current_stats['time']

    formatted_time: str

    if timespan != 0:
        minutes = int(timespan / 60)
        seconds = int(timespan % 60)
        if minutes >= 1:
            formatted_time = '{0} mins and {1} secs'.format(minutes, seconds)
        else:
            formatted_time = '{0} secs'.format(seconds)
    else:
        formatted_time = '0 secs'

    formatted_stats: str = '{0} steps in {1}'.format(distance, formatted_time)

    return formatted_stats


def save_dict_as_json(json_object: dict) -> None:
    with open(config.STATS_PATH, mode='w') as file:
        json.dump(json_object, file,
                  indent=2)  # Prettify json


def sum_new_stats(steps: int, walking_time: int) -> dict:
    stats = get_stats_dict()
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
        stats = get_stats_dict()
        stats['time'] = 0
        stats['distance'] = 0
        save_dict_as_json(stats)
