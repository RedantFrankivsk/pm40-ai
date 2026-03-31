import random

from discovery_engine import DiscoveryEngine
from experiment_engine import ExperimentEngine


class IdeaEngine:

    def __init__(self):

        self.discovery = DiscoveryEngine()
        self.experiment_engine = ExperimentEngine()

    def generate_strategy_ideas(self, count=5):

        patterns = self.discovery.generate_patterns(count)

        directions = [
            "follow_trend",
            "reversal",
            "breakout"
        ]

        risks = [
            "fixed",
            "adaptive",
            "dynamic"
        ]

        ideas = []

        for p in patterns:

            idea = {

                "pattern": p,

                "direction": random.choice(directions),

                "risk": random.choice(risks)

            }

            ideas.append(idea)

        return ideas

    def create_experiments_from_ideas(self, count=5):

        ideas = self.generate_strategy_ideas(count)

        experiments = []

        for idea in ideas:

            exp = {

                "pattern": idea["pattern"],
                "direction": idea["direction"],
                "risk": idea["risk"],
                "trades": 0,
                "wins": 0,
                "winrate": 0,
                "status": "testing"
            }

            experiments.append(exp)

        existing = self.experiment_engine.load()

        existing.extend(experiments)

        self.experiment_engine.save(existing)

        return experiments