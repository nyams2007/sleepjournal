# === Stage 3: Хранилище в памяти ===
# Project: SleepJournal
memory_store.py

from datetime import date


class Night:
    def __init__(self, id, sleep_date, duration_minutes, quality, wakeups):
        self.id = id
        self.sleep_date = sleep_date
        self.duration_minutes = duration_minutes
        self.quality = quality
        self.wakeups = wakeups

    def to_dict(self):
        return {
            "id": self.id,
            "sleep_date": self.sleep_date.isoformat() if isinstance(self.sleep_date, date) else self.sleep_date,
            "duration_minutes": self.duration_minutes,
            "quality": self.quality,
            "wakeups": self.wakeups,
        }

    @classmethod
    def from_dict(cls, data):
        sleep_date = data["sleep_date"]
        if isinstance(sleep_date, str):
            sleep_date = date.fromisoformat(sleep_date)
        return cls(
            id=data["id"],
            sleep_date=sleep_date,
            duration_minutes=data["duration_minutes"],
            quality=data["quality"],
            wakeups=data["wakeups"],
        )


class MemoryNightStore:
    def __init__(self):
        self._store = {}
        self._counter = 0

    def add(self, sleep_date, duration_minutes, quality, wakeups):
        self._counter += 1
        night = Night(
            id=self._counter,
            sleep_date=sleep_date,
            duration_minutes=duration_minutes,
            quality=quality,
            wakeups=wakeups,
        )
        self._store[night.id] = night
        return night

    def get(self, night_id):
        return self._store.get(night_id)

    def list_all(self):
        return list(self._store.values())

    def __len__(self):
        return len(self._store)
