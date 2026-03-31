import json
import os
import random

from pattern_memory import PatternMemory


class StrategyAutoEvolutionEngine:

    def __init__(self, file_path="auto_strategies.json"):

        self.file_path = file_path
        self.memory = PatternMemory()

        self.strategies = self._load()

    # =========================
    # LOAD
    # =========================
    def _load(self):

        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    # =========================
    # SAVE
    # =========================
    def save(self, strategies):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(strategies, f, indent=4)

    # =========================
    # 🔥 BOOTSTRAP STRATEGIES
    # =========================
    def _bootstrap(self):

        print("[EVOLUTION] 🔥 Bootstrapping strategies...")

        base = [
            {"type": "trend_follow", "weight": 2},
            {"type": "breakout", "weight": 2},
            {"type": "volume_push", "weight": 1},
            {"type": "pullback", "weight": 2},
            {"type": "range_reversal", "weight": 1}
        ]

        return base

    # =========================
    # MUTATION
    # =========================
    def _mutate(self, strategy):

        new_strategy = strategy.copy()

        # випадкова мутація ваги
        new_strategy["weight"] += random.choice([-1, 1])

        # обмеження
        new_strategy["weight"] = max(1, min(3, new_strategy["weight"]))

        return new_strategy

    # =========================
    # EVOLVE
    # =========================
    def evolve(self):

        strategies = self.strategies

        # 🔥 якщо пусто → bootstrap
        if not strategies:
            strategies = self._bootstrap()

        patterns = self.memory.all_patterns()

        evolved = []

        for strat in strategies:

            # якщо нема патернів — просто мутуємо
            if not patterns:
                evolved.append(self._mutate(strat))
                continue

            # вибираємо випадковий патерн
            pattern = random.choice(patterns)

            trades = pattern.get("trades", 0)
            wins = pattern.get("wins", 0)

            winrate = wins / trades if trades > 0 else 0

            # 🔥 якщо хороший патерн → підсилюємо
            if winrate > 0.6 and trades > 5:
                strat["weight"] = min(strat["weight"] + 1, 3)

            # якщо поганий → мутуємо
            elif winrate < 0.4:
                strat = self._mutate(strat)

            evolved.append(strat)

        self.strategies = evolved

        return evolved