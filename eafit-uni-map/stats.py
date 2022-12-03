"""
Access and update the stats file.
"""

from json import load, dump

import config

from humanfriendly import format_timespan


def get_stats_dict() -> dict:
    """Returns time and distance as a dictionary."""
    with open(config.STATS_PATH, encoding="utf-8") as file:
        return load(file)


def get_formatted_stats(steps=None, seconds=None) -> str:
    """Returns a formatted string with mins and secs."""
    distance: str
    time: str

    if steps == None and seconds == None:
        current_stats = get_stats_dict()

        distance = str(current_stats["distance"])
        time = format_timespan(current_stats["time"])
    else:
        distance = str(steps)
        time = format_timespan(seconds)
    formatted_stats: str = f"{distance} steps in {time}"
    return formatted_stats


def update_stats(steps: int, walking_time: int) -> None:
    """Stores the new stats values for time and distance."""
    stats = get_stats_dict()
    stats["distance"] += steps
    stats["time"] += walking_time
    with open(config.STATS_PATH, mode="w", encoding="utf-8") as file:
        dump(stats, file, indent=2)  # Prettify json
