# === Stage 1: Каркас модуля ===
# Project: SleepJournal
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List


@dataclass
class Night:
    date: date
    duration_hours: float
    quality: str
    awakenings: int = 0


def _generate_nights(count: int = 7, start: date = date(2024, 1, 1)) -> List[Night]:
    nights: List[Night] = []
    days_of_week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    for i in range(count):
        night = Night(
            date=start + timedelta(days=i),
            duration_hours=round(6.0 + (i % 3) * 0.5, 1),
            quality=f"Удовл.{days_of_week[i]}" if i < 5 else "Отлично",
            awakenings=i % 3,
        )
        nights.append(night)
    return nights


def main() -> None:
    nights = _generate_nights()
    total = sum(n.duration_hours for n in nights)
    avg = round(total / len(nights), 1)
    print("Дневник сна: демонстрационные записи")
    for n in nights:
        print(f"{n.date} | {n.duration_hours} ч | {n.quality} | пробуждений: {n.awakenings}")
    print(f"Итого: {total} ч за {len(nights)} ночей, в среднем {avg} ч/ночь")


if __name__ == "__main__":
    main()
