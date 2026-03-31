# =========================
# PATTERN PIPELINE (SMART FIX)
# =========================

from pattern_engine import build_pattern
from pattern_weight_engine import PatternWeightEngine


class PatternPipeline:

    def __init__(self):

        self.weight_engine = PatternWeightEngine()

    def normalize(self, pattern):

        if not pattern:
            return "empty_pattern"

        tokens = pattern.split()
        tokens = sorted(tokens)

        return " ".join(tokens)

    def build(self, tf_features, context):

        # 🔥 FIX: тільки M15 / M30 / H1
        pattern = build_pattern(
            trend_15m=tf_features["M15"]["trend"],
            trend_30m=tf_features["M30"]["trend"],
            trend_1h=tf_features["H1"]["trend"],
            structure=tf_features["M15"]["structure"],
            volume=context.get("volume", "normal_volume"),
            market_regime=context.get("regime", "unknown"),
            atr=context.get("atr", 0),
            price=context.get("price", 0),
            hour=context.get("hour", 0),
            trend_score=context.get("trend_score", 0)
        )

        pattern = self.normalize(pattern)

        if not pattern or len(pattern) < 5:
            pattern = f"fallback_{context.get('regime', 'unknown')}"

        print(f"[PATTERN] {pattern}")

        return pattern

    def apply(self, pattern, signal, confidence):

        signal, confidence = self.weight_engine.adjust_confidence(
            pattern,
            signal,
            confidence
        )

        return signal, confidence

    def update(self, pattern, result):

        self.weight_engine.update(pattern, result)