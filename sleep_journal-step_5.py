# === Stage 5: Связанная сущность ===
# Project: SleepJournal
from datetime import date


class SleepFactor:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"SleepFactor(name={self.name!r}, value={self.value!r})"


class SleepJournal:
    def __init__(self):
        self.factors = {}

    def add_factor(self, factor):
        self.factors[factor.name] = factor

    def get_factor(self, name):
        return self.factors.get(name)
