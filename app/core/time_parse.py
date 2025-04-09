from datetime import datetime


def datetime_parse(date_str: str) -> datetime | None:
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return datetime.now()
