from experiment_evaluator import ExperimentEvaluator

engine = ExperimentEvaluator()

promoted, failed = engine.evaluate()

print()
print("=== EXPERIMENT EVALUATION ===")
print()

print("Promoted:", len(promoted))
print("Failed:", len(failed))

print()