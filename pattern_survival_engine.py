import json
from edge_confidence_engine import EdgeConfidenceEngine
from pattern_memory import PatternMemory


class PatternSurvivalEngine:

    def __init__(self):

        self.memory = PatternMemory()
        self.conf_engine = EdgeConfidenceEngine()

        self.min_trades = 5
        self.min_confidence = 0.2

        self.output_file = "pattern_population.json"

    def evaluate_population(self):

        edges = self.conf_engine.analyze()

        survivors = []
        extinct = []

        for e in edges:

            pattern = e["pattern"]
            trades = e["trades"]
            confidence = e["confidence"]

            if trades < self.min_trades:
                continue

            if confidence >= self.min_confidence:

                survivors.append({
                    "pattern": pattern,
                    "trades": trades,
                    "winrate": e["winrate"],
                    "confidence": confidence
                })

            else:

                extinct.append({
                    "pattern": pattern,
                    "trades": trades,
                    "confidence": confidence
                })

        population = {

            "survivors": survivors,
            "extinct": extinct
        }

        with open(self.output_file, "w") as f:

            json.dump(population, f, indent=4)

        return population