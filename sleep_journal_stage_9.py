# === Stage 9: Текстовый поиск ===
# Project: SleepJournal
def search_nights(nights, query, case_insensitive=True):
    """Поиск ночей по текстовым полям с подсветкой совпадений.

    Ищет в полях date, quality и wakeups. Подсветка реализуется через
    замену совпадений на последовательность символов-маркеров.
    """
    fields = ("date", "quality", "wakeups")
    lowered = query.lower() if case_insensitive else query
    marker = " «» "
    results = []

    for night in nights:
        text = " ".join(
            str(getattr(night, field, "")) for field in fields
        )
        if lowered and lowered in text.lower():
            highlighted = _highlight(text, query, case_insensitive)
            results.append(
                {
                    "night": night,
                    "match": highlighted,
                    "query": query,
                }
            )
    return results


def _highlight(text, query, case_insensitive):
    """Возвращает строку с выделенными совпадениями маркером «»."""
    if not query:
        return text
    lowered = text.lower() if case_insensitive else text
    needle = query.lower() if case_insensitive else query
    out = []
    start = 0
    index = 0
    while True:
        pos = lowered.find(needle, start)
        if pos == -1:
            out.append(text[start:])
            break
        out.append(text[start:pos])
        out.append(marker)
        start = pos + len(needle)
        index = start
    return "".join(out)


if __name__ == "__main__":
    nights = [
        {"date": "2024-01-05", "quality": "плохой", "wakeups": 3},
        {"date": "2024-01-06", "quality": "хороший", "wakeups": 0},
        {"date": "2024-01-07", "quality": "средний", "wakeups": 2},
    ]
    for hit in search_nights(nights, "хорош"):
        print(hit["night"]["date"], "->", hit["match"])
