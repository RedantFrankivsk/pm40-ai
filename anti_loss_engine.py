# anti_loss_engine.py

from pattern_memory import PatternMemory


class AntiLossEngine:

    def __init__(self):

        self.memory = PatternMemory()

        # 🔥 BALANCED SETTINGS
        self.min_confidence = 45
        self.min_trades_for_pattern = 10
        self.min_winrate = 0.48   # не душимо, але вже відсіюємо повний шлак

    def check_tf_conflict(self, results):

        signals = [r["signal"] for r in results]

        if signals.count("UP") > 0 and signals.count("DOWN") > 0:
            return False, "tf_conflict"

        return True, None

    def check_confidence(self, confidence):

        if confidence < self.min_confidence:
            return False, "low_confidence"

        return True, None

    def check_pattern_quality(self, tf_features, signal):

        pattern_key = str(tf_features) + "_" + signal

        stats = self.memory.get_pattern_stats(pattern_key)

        trades = stats["trades"]
        wins = stats["wins"]

        if trades < self.min_trades_for_pattern:
            # 🔥 мало даних → НЕ блокуємо
            return True, None

        winrate = wins / trades if trades > 0 else 0

        if winrate < self.min_winrate:
            return False, f"bad_pattern_winrate ({round(winrate, 2)})"

        return True, None

    def check_all_neutral(self, results):

        if all(r["signal"] == "NEUTRAL" for r in results):
            return False, "all_neutral"

        return True, None

    def run(self, results, confidence, final_signal, tf_features):

        # 1. TF conflict
        ok, reason = self.check_tf_conflict(results)
        if not ok:
            return False, reason

        # 2. Confidence
        ok, reason = self.check_confidence(confidence)
        if not ok:
            return False, reason

        # 3. Neutral filter
        ok, reason = self.check_all_neutral(results)
        if not ok:
            return False, reason

        # 4. 🔥 Pattern quality (NEW CORE)
        ok, reason = self.check_pattern_quality(tf_features, final_signal)
        if not ok:
            return False, reason

        return True, None


# =========================
# GLOBAL FUNCTION (для сумісності)
# =========================

_engine = AntiLossEngine()


def anti_loss_filter(results, confidence, final_signal, tf_features=None):

    # fallback якщо не передали tf_features
    if tf_features is None:
        tf_features = {}

    return _engine.run(results, confidence, final_signal, tf_features)