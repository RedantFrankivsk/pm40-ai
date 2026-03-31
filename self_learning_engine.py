# =========================
# PM40 SELF LEARNING ENGINE (HARD FIX)
# =========================

from meta_learning_engine import MetaLearningEngine
from pattern_memory import PatternMemory


class SelfLearningEngine:

    def __init__(self):
        self.meta = MetaLearningEngine()
        self.memory = PatternMemory()

    def normalize_pattern(self, pattern):
        """
        🔥 FIX ANY TYPE → HASHABLE STRING
        """

        try:
            if isinstance(pattern, list):
                return "|".join([self.normalize_pattern(p) for p in pattern])

            if isinstance(pattern, dict):
                return "|".join([f"{k}:{self.normalize_pattern(v)}" for k, v in sorted(pattern.items())])

            return str(pattern)

        except Exception as e:
            print("[NORMALIZE ERROR]", e)
            return str(pattern)

    def update_pattern_memory(self):

        stats = self.meta.pattern_stats()

        print("[SELF-LEARNING] Updating PatternMemory...")

        for s in stats:

            raw_pattern = s.get("pattern", "unknown")
            pattern = self.normalize_pattern(raw_pattern)

            self.memory.patterns[pattern] = {
                "trades": s.get("trades", 0),
                "wins": s.get("wins", 0)
            }

        self.memory.save()

    def run(self):

        print("\n🧠 SELF-LEARNING START")

        try:
            self.update_pattern_memory()
            print("[SELF-LEARNING] Pattern memory updated")

        except Exception as e:
            print("[SELF-LEARNING ERROR]", e)

        print("🧠 SELF-LEARNING END\n")