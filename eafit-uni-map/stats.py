from json import load, dump

import config


def get_stats_dict() -> dict:
    with open(config.STATS_PATH, encoding="utf-8") as file:
        return load(file)


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


def update_stats(steps: int, walking_time: int) -> None:
    stats = get_stats_dict()
    stats["distance"] += steps
    stats["time"] += walking_time
    with open(config.STATS_PATH, mode="w", encoding="utf-8") as file:
        dump(stats, file, indent=2)  # Prettify json
