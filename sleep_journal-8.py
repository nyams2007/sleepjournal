# === Stage 8: Сортировка записей ===
# Project: SleepJournal
import datetime


def by_date(record):
    date_value = record.get("date")
    if isinstance(date_value, str):
        date_value = datetime.date.fromisoformat(date_value)
    return date_value


def by_created_at(record):
    return record.get("created_at")


def sort_nights(records, key=by_date, reverse=False):
    return sorted(records, key=key, reverse=reverse)
