# =========================
# PM40 PATTERN WEIGHT ENGINE
# =========================

from pattern_memory import PatternMemory
from pattern_score_engine import PatternScoreEngine
from pattern_normalizer import PatternNormalizer


class PatternWeightEngine:

    def __init__(self):

        self.memory = PatternMemory()
        self.scorer = PatternScoreEngine()
        self.normalizer = PatternNormalizer()

        self.min_trades = 5

    def get_weight(self, pattern: str):

        key = self.normalizer.normalize(pattern)

        stats = self.memory.get_pattern_stats(key)

        trades = stats.get("trades", 0)
        wins = stats.get("wins", 0)

        # 🔥 якщо мало даних — не нейтраль, а легкий буст
        if trades < self.min_trades:
            return 1.05

        score = self.scorer.calculate(trades, wins)

        # 🔥 більш плавна шкала (було занадто різко)
        if score > 0.3:
            return 1.35

        if score > 0.15:
            return 1.2

        if score > 0.05:
            return 1.1

        if score < -0.3:
            return 0.5

        if score < -0.15:
            return 0.7

        if score < -0.05:
            return 0.85

        return 1.0

    def adjust_confidence(self, pattern, signal, confidence):

        weight = self.get_weight(pattern)

        new_conf = confidence * weight

        print(f"[PATTERN WEIGHT] {pattern} → weight={weight:.2f}")

        # 🔥 якщо патерн реально слабкий — гасимо
        if weight < 0.7 and confidence < 65:
            print("[PATTERN WEIGHT] ❌ weak pattern → NEUTRAL")
            return "NEUTRAL", new_conf

        new_conf = max(0, min(100, new_conf))

        return signal, new_conf

    def update(self, pattern, result):

        key = self.normalizer.normalize(pattern)

        self.memory.update(key, result)