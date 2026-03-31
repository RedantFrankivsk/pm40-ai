from mutation_experiment_engine import MutationExperimentEngine


engine = MutationExperimentEngine()

results = engine.run()

print()
print("=== PM40 MUTATION EXPERIMENTS ===")
print()

for r in results:

    if r["tested"]:

        print(
            r["pattern"],
            "| trades:", r["trades"],
            "| winrate:", r["winrate"]
        )