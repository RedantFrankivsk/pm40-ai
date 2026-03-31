from experiment_engine import ExperimentEngine

engine = ExperimentEngine()

new_experiments = engine.generate_experiments()

print()
print("=== PM40 EXPERIMENT LAB ===")
print()

print("New experiments:", len(new_experiments))
print()

for e in new_experiments:

    print(
        e["pattern"],
        "| direction:", e["direction"],
        "| risk:", e["risk"]
    )

print()