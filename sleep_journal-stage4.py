# === Stage 4: Удаление и восстановление ===
# Project: SleepJournal
"""SleepJournal: мягкое удаление сущности «ночь» и восстановление.

Этап 4 из 81. Самодостаточный модуль: свои импорты и вспомогательные
определения, только стандартная библиотека.

Предполагается, что:
  * класс Night определён в этом же модуле (или импортирован из другого),
    либо создан как локальный класс ниже;
  * у Night есть атрибуты: date, duration, quality, awakenings,
    а также атрибут soft_deleted (bool) и список deleted_nights (в Night).
"""

import copy
import datetime


class SoftDeleteRegistry:
    """Хранит «мягко» удалённые ночи и позволяет их восстанавливать.

    Soft-удаление не выбрасывает сущность из хранилища, а помечает её
    атрибутом soft_deleted и переносит в отдельный список deleted_nights.
    Так дневник остаётся неизменным по размеру, а пользователь может
    вернуть удалённые записи в любой момент.
    """

    def __init__(self):
        self.deleted_nights = []

    def soft_delete(self, night):
        """Помечает ночь как удалённую и переносит её в хранилище."""
        night.soft_deleted = True
        self.deleted_nights.append(night)

    def restore(self, night):
        """Восстанавливает ночь: снимает флаг и возвращает в журнал."""
        if night in self.deleted_nights:
            self.deleted_nights.remove(night)
            night.soft_deleted = False
            return True
        return False

    def restore_all(self):
        """Восстанавливает все мягко удалённые ночи за раз."""
        for night in list(self.deleted_nights):
            self.restore(night)
        return len(self.deleted_nights)

    def is_deleted(self, night):
        """Проверяет, была ли ночь мягко удалена."""
        return night in self.deleted_nights

    def count_deleted(self):
        """Возвращает количество мягко удалённых ночей."""
        return len(self.deleted_nights)

    def find_deleted(self, date):
        """Находит мягко удалённую ночь по дате (для предпросмотра)."""
        for night in self.deleted_nights:
            if night.date == date:
                return night
        return None


class Night:
    """Ночь сна с поддержкой мягкого удаления.

    Класс определён локально, чтобы модуль был самодостаточным: он может
    использоваться как самостоятельная сущность или расширять существующую.
    """

    QUALITY_SCALE = {"excellent": 5, "good": 4, "average": 3, "poor": 2, "very_poor": 1}

    def __init__(self, date, duration, quality, awakenings=0):
        self.date = date
        self.duration = duration
        self.quality = quality
        self.awakenings = awakenings
        self.soft_deleted = False

    def to_dict(self):
        return {
            "date": self.date,
            "duration": self.duration,
            "quality": self.quality,
            "awakenings": self.awakenings,
            "soft_deleted": self.soft_deleted,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            date=data.get("date"),
            duration=data.get("duration"),
            quality=data.get("quality"),
            awakenings=data.get("awakenings", 0),
        )

    def average_quality_score(self):
        return self.QUALITY_SCALE.get(self.quality, 3)

    def __repr__(self):
        status = " (удалена)" if self.soft_deleted else ""
        return f"Night({self.date}, {self.duration} мин, {self.quality}){status}"


if __name__ == "__main__":
    registry = SoftDeleteRegistry()

    night1 = Night(date=datetime.date(2025, 1, 5), duration=420, quality="good", awakenings=1)
    night2 = Night(date=datetime.date(2025, 1, 6), duration=300, quality="average", awakenings=3)

    registry.soft_delete(night1)
    print("Удалено ночей:", registry.count_deleted())

    preview = registry.find_deleted(datetime.date(2025, 1, 5))
    if preview:
        print("Предпросмотр:", preview)

    registry.restore(night1)
    print("Восстановлено:", registry.count_deleted() == 0)

    night3 = Night(date=datetime.date(2025, 1, 7), duration=500, quality="excellent")
    registry.soft_delete(night3)
    registry.restore_all()
    print("После восстановления всех:", registry.count_deleted(), "удалённых")
