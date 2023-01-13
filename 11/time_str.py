def getHoursMinutesSeconds(seconds: int) -> str:
    if seconds == 0:
        return "0s"
    result_values = []
    time_per_unit = [(86400, "d"), (3600, "h"), (60, "m"), (1, "s")]
    for duration, unit in time_per_unit:
        n = seconds // duration
        seconds = seconds % duration
        if n:
            result_values.append(f"{n}{unit}")
    return " ".join(result_values)
