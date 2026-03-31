import random
from market_simulation_engine import MarketSimulationEngine
from market_physics_engine import MarketPhysicsEngine
from brain_committee import BrainCommittee


class SelfPlayTrainingEngine:

    def __init__(self):

        self.market = MarketSimulationEngine()
        self.physics = MarketPhysicsEngine()
        self.brain = BrainCommittee()

    def run(self, trades=100):

        results = []

        for _ in range(trades):

            pattern, context, regime = self.market.generate_market()

            decision = self.brain.decide(pattern, context, regime)

            signal = decision["final_signal"]

            best_brain = None
            best_conf = -1

            for vote in decision["votes"]:

                if vote["confidence"] > best_conf:
                    best_conf = vote["confidence"]
                    best_brain = vote["brain"]

            result = self.physics.evaluate_trade(signal, regime)

            trade = {
                "pattern": pattern,
                "context": context,
                "regime": regime,
                "signal": signal,
                "brain": best_brain,
                "confidence": best_conf,
                "result": result
            }

            results.append(trade)

        return results