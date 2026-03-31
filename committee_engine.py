# =========================
# PM40 COMMITTEE ENGINE (FULL)
# =========================

from brain_committee import BrainCommittee


class CommitteeEngine:

    def __init__(self):

        self.committee = BrainCommittee()

    def decide(self, pattern, context, regime):

        pattern_tokens = pattern.split()
        context_tokens = list(context.values())

        result = self.committee.decide(
            pattern_tokens,
            context_tokens,
            regime
        )

        votes = result["votes"]

        up = 0
        down = 0

        for v in votes:

            weight = v.get("weight", 1.0)

            if v["signal"] == "UP":
                up += weight

            elif v["signal"] == "DOWN":
                down += weight

        if up > down:
            final_signal = "UP"
        elif down > up:
            final_signal = "DOWN"
        else:
            final_signal = "NEUTRAL"

        confidence = abs(up - down) / max(1.0, (up + down))

        confidence = round(confidence * 100, 2)

        return {
            "signal": final_signal,
            "confidence": confidence,
            "votes": votes
        }