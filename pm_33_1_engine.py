import math

class Pattern:
    def __init__(self, name):
        self.name = name
        self.trust = 0.5
        self.samples = 0
        self.wins = 0
        self.losses = 0
        self.neutrals = 0

    def update_outcome(self, outcome):
        self.samples += 1
        if outcome == "WIN":
            self.wins += 1
            self.trust = min(1.0, self.trust + 0.1)
        elif outcome == "LOSS":
            self.losses += 1
            self.trust = max(0.0, self.trust - 0.1)
        else:
            self.neutrals += 1

    def confidence(self, signal_strength):
        return abs(signal_strength) * self.trust


class PM33Engine:
    def __init__(self):
        self.pattern_a = Pattern("A")
        self.pattern_b = Pattern("B")

    def entropy(self, conf_a, conf_b):
        if conf_a == 0 and conf_b == 0:
            return 1.0
        diff = abs(conf_a - conf_b)
        return round(1 / (1 + diff), 3)

    def decide(self, impulse, volume):
        # --- Pattern A (Impulse based) ---
        sig_a = 0
        if abs(impulse) > 0.4:
            sig_a = -1 if impulse < 0 else 1

        conf_a = self.pattern_a.confidence(impulse)

        # --- Pattern B (Volume based) ---
        sig_b = 0
        if abs(volume) > 0.4:
            sig_b = -1 if volume < 0 else 1

        conf_b = self.pattern_b.confidence(volume)

        entropy = self.entropy(conf_a, conf_b)

        decision = "NEUTRAL"
        status = "BLOCKED"
        confidence = 0.0

        if sig_a != 0 and sig_a == sig_b:
            decision = "UP" if sig_a == 1 else "DOWN"
            confidence = round((conf_a + conf_b) / 2, 3)
            status = "CONFIRMED"

        elif sig_a != 0 and conf_a > conf_b:
            decision = "UP" if sig_a == 1 else "DOWN"
            confidence = round(conf_a, 3)
            status = "A_SOLO"

        elif sig_b != 0 and conf_b > conf_a:
            decision = "UP" if sig_b == 1 else "DOWN"
            confidence = round(conf_b, 3)
            status = "B_SOLO"

        return {
            "decision": decision,
            "confidence": confidence,
            "status": status,
            "entropy": entropy,
            "trust_a": round(self.pattern_a.trust, 3),
            "trust_b": round(self.pattern_b.trust, 3),
        }
