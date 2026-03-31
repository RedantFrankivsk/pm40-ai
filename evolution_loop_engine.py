from autonomous_research_loop import AutonomousResearchLoop
from experiment_engine import ExperimentEngine
from experiment_evaluator import ExperimentEvaluator
from curiosity_engine import CuriosityEngine
from discovery_engine import DiscoveryEngine
from idea_engine import IdeaEngine


class EvolutionLoopEngine:

    def __init__(self):

        self.research = AutonomousResearchLoop()
        self.experiments = ExperimentEngine()
        self.evaluator = ExperimentEvaluator()
        self.curiosity = CuriosityEngine()
        self.discovery = DiscoveryEngine()
        self.idea = IdeaEngine()

    def run(self):

        print()
        print("=== PM40 EVOLUTION LOOP START ===")
        print()

        # research cycle
        report = self.research.run_cycle()

        print("Brain status:", report["brain_status"]["status"])
        print()

        # evaluate experiments
        promoted, failed = self.evaluator.evaluate()

        print("Experiments promoted:", len(promoted))
        print("Experiments failed:", len(failed))
        print()

        # curiosity
        rare = self.curiosity.find_rare_patterns()

        print("Rare patterns found:", len(rare))
        print()

        # discovery
        new_patterns = self.discovery.generate_patterns()

        print("Discovered patterns:", len(new_patterns))
        print()

        # idea generation
        ideas = self.idea.create_experiments_from_ideas()

        print("New experiment ideas:", len(ideas))
        print()

        print("=== PM40 EVOLUTION LOOP END ===")
        print()