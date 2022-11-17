import json

import config


def get_stats_dict() -> dict:
    with open(config.STATS_PATH, encoding="utf-8") as file:
        return json.load(file)


def get_formatted_stats() -> str:
    current_stats = get_stats_dict()

    distance = str(current_stats["distance"])
    timespan: int = current_stats["time"]

    formatted_time: str

    if timespan != 0:
        minutes = int(timespan / 60)
        seconds = int(timespan % 60)
        if minutes >= 1:
            formatted_time = f"{minutes} mins and {seconds} secs"
        else:
            formatted_time = f"{seconds} secs"
    else:
        formatted_time = "0 secs"

    formatted_stats: str = f"{distance} steps in {formatted_time}"

    return formatted_stats


def save_dict_as_json(json_object: dict) -> None:
    with open(config.STATS_PATH, mode="w", encoding="utf-8") as file:
        json.dump(json_object, file, indent=2)  # Prettify json


def sum_new_stats(steps: int, walking_time: int) -> dict:
    stats = get_stats_dict()
    stats["distance"] += steps
    stats["time"] += walking_time
    return stats


def update_stats(steps: int, walking_time: int) -> None:
    # This seems redundant, but I find it better to decompose
    new_stats = sum_new_stats(steps, walking_time)
    save_dict_as_json(new_stats)
