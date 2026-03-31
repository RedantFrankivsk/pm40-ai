# Pattern B: Impulse + Volume (independent)

from dataclasses import dataclass
import math

@dataclass
class PatternBResult:
    signal: str          # UP / DOWN / NEUTRAL
    confidence: float    # 0..1
    entropy: float       # 0..1
    active: bool


class PatternBImpulse:
    def __init__(self):
        self.history = []

    def _entropy(self, p_up, p_down):
        eps = 1e-9
        p_neu = max(0.0, 1.0 - p_up - p_down)
        ent = 0.0
        for p in (p_up, p_down, p_neu):
            if p > 0:
                ent -= p * math.log2(p + eps)
        return min(ent / math.log2(3), 1.0)

    def evaluate(self, impulse_strength, volume_delta):
        """
        impulse_strength: float (-1 .. +1)
        volume_delta: float (-1 .. +1)
        """

        score = impulse_strength * volume_delta

        if abs(score) < 0.2:
            return PatternBResult(
                signal="NEUTRAL",
                confidence=0.0,
                entropy=1.0,
                active=False
            )

        signal = "UP" if score > 0 else "DOWN"
        confidence = min(abs(score), 1.0)

        p_up = confidence if signal == "UP" else 0.0
        p_down = confidence if signal == "DOWN" else 0.0
        entropy = self._entropy(p_up, p_down)

        return PatternBResult(
            signal=signal,
            confidence=confidence,
            entropy=entropy,
            active=True
        )
