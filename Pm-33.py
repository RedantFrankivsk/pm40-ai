# PM-33.2 FULL CODE
# Change: Agent B is no longer a mirror of A.
# A = impulse-dominant, B = volume-dominant + damping

import random
import math

class Agent:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode  # 'impulse' or 'volume'
        self.trust = 0.5

    def decide(self, impulse, volume):
        if self.mode == 'impulse':
            score = impulse
        else:
            # volume agent reacts weaker + smooth
            score = volume * 0.6 - impulse * 0.2

        if score > 0.2:
            return 'UP', abs(score)
        elif score < -0.2:
            return 'DOWN', abs(score)
        else:
            return 'NEUTRAL', 0.0

    def update_trust(self, outcome):
        if outcome == 'WIN':
            self.trust = min(1.0, self.trust + 0.1)
        elif outcome == 'LOSS':
            self.trust = max(0.0, self.trust - 0.1)


def entropy_from_conf(conf):
    return round(1.0 - conf + random.uniform(-0.05, 0.05), 3)


def resolve(a_dec, b_dec, a_conf, b_conf, a_trust, b_trust):
    if a_dec == b_dec and a_dec != 'NEUTRAL':
        conf = round((a_conf * a_trust + b_conf * b_trust), 3)
        return a_dec, conf, 'CONFIRMED'

    if a_trust > b_trust and a_dec != 'NEUTRAL':
        return a_dec, round(a_conf * a_trust, 3), 'A_SOLO'

    if b_trust > a_trust and b_dec != 'NEUTRAL':
        return b_dec, round(b_conf * b_trust, 3), 'B_SOLO'

    return 'NEUTRAL', 0.0, 'BLOCKED'


print("=== SIMULATION PM-33.2 START ===")

A = Agent('A', 'impulse')
B = Agent('B', 'volume')

for step in range(1, 11):
    print(f"\n--- STEP {step} ---")

    impulse = round(random.uniform(-1, 1), 2)
    volume = round(random.uniform(-1, 1), 2)

    a_dec, a_conf = A.decide(impulse, volume)
    b_dec, b_conf = B.decide(impulse, volume)

    decision, conf, status = resolve(a_dec, b_dec, a_conf, b_conf, A.trust, B.trust)

    outcome = random.choice(['WIN', 'LOSS', 'NEUTRAL'])

    if status == 'A_SOLO':
        A.update_trust(outcome)
    elif status == 'B_SOLO':
        B.update_trust(outcome)
    elif status == 'CONFIRMED':
        A.update_trust(outcome)
        B.update_trust(outcome)

    entropy = entropy_from_conf(conf)

    print(f"OUTCOME: {outcome}")
    print(f"IMPULSE: {impulse} | VOLUME: {volume}")
    print(f"DECISION: {decision}")
    print(f"CONF: {conf}")
    print(f"STATUS: {status}")
    print(f"ENTROPY: {entropy}")
    print(f"TRUST A/B: {round(A.trust,2)} / {round(B.trust,2)}")