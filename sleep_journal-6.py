# === Stage 6: Связи между сущностями ===
# Project: SleepJournal
from datetime import date


class SleepFactor:
    """Фактор, влияющий на качество сна за одну ночь."""

    def __init__(self, name, value, night):
        self.name = name
        self.value = value
        self.night = night

    def __repr__(self):
        return f"SleepFactor({self.name!r}, {self.value!r})"


class Night:
    """Ночь сна с факторами, влияющими на её качество."""

    def __init__(self, date, duration, quality, awakenings):
        self.date = date
        self.duration = duration
        self.quality = quality
        self.awakenings = awakenings
        self.factors = []

    def add_factor(self, factor):
        if not isinstance(factor, SleepFactor):
            raise TypeError("Фактор должен быть объектом SleepFactor")
        if factor.night is not self:
            raise ValueError("Фактор привязан к другой ночи")
        self.factors.append(factor)


def get_factors_for_night(night):
    """Возвращает все факторы для указанной ночи в порядке добавления."""
    if not isinstance(night, Night):
        raise TypeError("Аргумент должен быть объектом Night")
    return list(night.factors)


def verify_factor_integrity(night):
    """
    Проверяет целостность связи между ночью и её факторами.

    Проверяет, что все факторы принадлежат ночи, и что у ночи есть
    хотя бы один фактор. Возвращает список проблем или пустой список
    при успешной проверке.
    """
    problems = []

    if night.factors:
        problems.append("Ночь не имеет факторов")

    for factor in night.factors:
        if factor.night is not night:
            problems.append(f"Фактор {factor.name!r} не привязан к ночи")

    return problems


def assert_factors_consistent(night):
    """Проверяет целостность и поднимает ValueError при обнаружении проблем."""
    problems = verify_factor_integrity(night)
    if problems:
        raise ValueError("; ".join(problems))
    return True
