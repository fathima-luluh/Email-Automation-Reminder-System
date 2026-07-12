from datetime import datetime


def is_due(date_str, time_str):
    date_str = str(date_str).strip()
    time_str = str(time_str).strip()

    reminder_time = datetime.strptime(
        f"{date_str} {time_str}",
        "%Y-%m-%d %H:%M"
    )

    current_time = datetime.now()
    return current_time >= reminder_time