# =========================
# PM40 META LEARNING ENGINE (SAFE)
# =========================

class MetaLearningEngine:

    def __init__(self):
        self.memory = {}

    # =========================
    # NORMALIZE KEY
    # =========================
    def normalize_key(self, key):

        if isinstance(key, list):
            return "|".join([self.normalize_key(k) for k in key])

        if isinstance(key, dict):
            return "|".join([
                f"{k}:{self.normalize_key(v)}"
                for k, v in sorted(key.items())
            ])

        return str(key)

    # =========================
    # ADD EVENT (якщо є десь виклик)
    # =========================
    def add(self, pattern, result):

        key = self.normalize_key(pattern)

        if key not in self.memory:
            self.memory[key] = {
                "trades": 0,
                "wins": 0
            }

        self.memory[key]["trades"] += 1

        if result == "WIN":
            self.memory[key]["wins"] += 1

    # =========================
    # GET STATS (🔥 ГОЛОВНИЙ ФІКС)
    # =========================
    def pattern_stats(self):

        result = []

        for key, stats in self.memory.items():

            safe_key = self.normalize_key(key)

            result.append({
                "pattern": safe_key,
                "trades": stats.get("trades", 0),
                "wins": stats.get("wins", 0)
            })

        return result