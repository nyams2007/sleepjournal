# === Stage 7: Генерация идентификаторов ===
# Project: SleepJournal
import uuid
import random


PREFIX = "sleep"


def generate_id():
    """Генерирует уникальный идентификатор с префиксом проекта.

    Формат: sleep_<6 символов из таблицы>
    """
    alphabet = "abcdefghijkmnpqrstuvwxyz"
    while True:
        candidate = PREFIX + "".join(random.choice(alphabet) for _ in range(6))
        if not _is_available(candidate):
            continue
        return candidate


def _is_available(candidate):
    """Проверяет, не занят ли идентификатор в текущем журнале.

    Возвращает True, если идентификатор свободен.
    """
    for entry in _iter_entries():
        if getattr(entry, "id", None) == candidate:
            return False
    return True


def _iter_entries():
    """Перебирает существующие записи журнала сна.

    Использует глобальную коллекцию записей, если она определена,
    иначе перебирает данные из демо-файла, если он существует.
    """
    namespace = globals()
    if "entries" in namespace and namespace["entries"] is not None:
        for entry in namespace["entries"]:
            yield entry
    elif "demo_data" in namespace and namespace["demo_data"] is not None:
        for entry in namespace["demo_data"]:
            yield entry
    else:
        yield from []


def generate_unique_id():
    """Генерирует уникальный идентификатор с проверкой коллизий.

    Формат: sleep_<6 символов из таблицы>
    """
    alphabet = "abcdefghijkmnpqrstuvwxyz"
    while True:
        candidate = PREFIX + "".join(random.choice(alphabet) for _ in range(6))
        if not _is_available(candidate):
            continue
        return candidate
