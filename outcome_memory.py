class OutcomeMemory:

    def __init__(self):

        self.wins = 0
        self.losses = 0

        self.trust_a = 1.0
        self.trust_b = 1.0

        self.fatigue = 0.0

    def update(self, result):

        if result == "WIN":
            self.wins += 1
            self.trust_a = min(self.trust_a + 0.03, 1.5)
            self.fatigue = max(self.fatigue - 0.03, 0)

        elif result == "LOSS":
            self.losses += 1
            self.trust_b = max(self.trust_b - 0.03, 0.6)
            self.fatigue = min(self.fatigue + 0.03, 1)

    def get_trust_score(self):
        return (self.trust_a + self.trust_b) / 2

    def should_block(self):

        total = self.wins + self.losses

        if total < 5:
            return False  # 🔥 НЕ блокуємо на старті

        trust = self.get_trust_score()

        if trust < 0.7:
            return True

        if self.fatigue > 0.8:
            return True

        return False