from meta_learning_engine import MetaLearningEngine
from edge_reinforcement_engine import EdgeReinforcementEngine
from self_evolution_engine import SelfEvolutionEngine
from decision_calibration_engine import DecisionCalibrationEngine


class AutonomousResearchLoop:

    def __init__(self):

        self.meta_engine = MetaLearningEngine()
        self.edge_engine = EdgeReinforcementEngine()
        self.evolution_engine = SelfEvolutionEngine()
        self.calibration_engine = DecisionCalibrationEngine()

    def run_cycle(self):

        report = {}

        # META LEARNING
        pattern_stats = self.meta_engine.pattern_stats()
        strategy_stats = self.meta_engine.strategy_stats()
        regime_stats = self.meta_engine.regime_stats()

        report["patterns"] = pattern_stats
        report["strategies"] = strategy_stats
        report["regimes"] = regime_stats

        # EDGE REINFORCEMENT
        strongest_patterns = self.edge_engine.strongest_patterns()

        report["strongest_patterns"] = strongest_patterns

        # STRATEGY EVOLUTION
        new_strategies = self.evolution_engine.evolve()

        report["new_strategies"] = new_strategies

        # DECISION CALIBRATION
        calibration = self.calibration_engine.calibration_report()

        report["brain_status"] = calibration

        return report