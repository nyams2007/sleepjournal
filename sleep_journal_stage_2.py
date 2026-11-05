# === Stage 2: Проверка полей ===
# Project: SleepJournal
import datetime


FIELD_MESSAGES = {
    "date": "Укажите дату в формате ДД.ММ.ГГГГ (например, 15.06.2025).",
    "duration": "Укажите длительность сна в часах числом (например, 7.5).",
    "quality": "Укажите качество сна от 1 до 5.",
    "wakeup": "Укажите число пробуждений (неотрицательное целое число).",
}


def normalize_date(value):
    try:
        day, month, year = value.split(".")
        return datetime.date(int(year), int(month), int(day))
    except (ValueError, AttributeError):
        return None


def normalize_duration(value):
    try:
        result = float(value)
    except (ValueError, AttributeError):
        return None
    if result < 0 or result > 24:
        return None
    return result


def normalize_quality(value):
    try:
        result = int(value)
    except (ValueError, AttributeError):
        return None
    if result < 1 or result > 5:
        return None
    return result


def normalize_wakeup(value):
    try:
        result = int(value)
    except (ValueError, AttributeError):
        return None
    if result < 0:
        return None
    return result


def validate_night(date, duration, quality, wakeup):
    errors = []
    normalized = {}

    if not date:
        errors.append(FIELD_MESSAGES["date"])
    else:
        normalized["date"] = normalize_date(date)
        if normalized["date"] is None:
            errors.append(FIELD_MESSAGES["date"])

    if duration is None or duration == "":
        errors.append(FIELD_MESSAGES["duration"])
    else:
        normalized["duration"] = normalize_duration(duration)
        if normalized["duration"] is None:
            errors.append(FIELD_MESSAGES["duration"])

    if quality is None or quality == "":
        errors.append(FIELD_MESSAGES["quality"])
    else:
        normalized["quality"] = normalize_quality(quality)
        if normalized["quality"] is None:
            errors.append(FIELD_MESSAGES["quality"])

    if wakeup is None or wakeup == "":
        errors.append(FIELD_MESSAGES["wakeup"])
    else:
        normalized["wakeup"] = normalize_wakeup(wakeup)
        if normalized["wakeup"] is None:
            errors.append(FIELD_MESSAGES["wakeup"])

    return normalized, errors
