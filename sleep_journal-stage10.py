# === Stage 10: Поиск по нескольким словам ===
# Project: SleepJournal
def find_nights(entries, words, exclusions=None):
    exclusions = exclusions or []
    result = []
    for entry in entries:
        if any(exclusion in entry for exclusion in exclusions):
            continue
        if all(word in entry for word in words):
            result.append(entry)
    return result

if __name__ == "__main__":
    sample = [
        {"date": "2024-01-01", "quality": "good", "note": "restful night"},
        {"date": "2024-01-02", "quality": "bad", "note": "noisy neighbors"},
        {"date": "2024-01-03", "quality": "good", "note": "deep sleep"},
        {"date": "2024-01-04", "quality": "fair", "note": "restless night"},
    ]
    print(find_nights(sample, ["good"]))
    print(find_nights(sample, ["good"], ["restless"]))
