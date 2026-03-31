from mutation_selection_engine import MutationSelectionEngine


engine = MutationSelectionEngine()

selected = engine.run()

print()
print("=== PM40 SELECTED STRATEGIES ===")
print()

for s in selected:

    print(
        s["pattern"],
        "| experiment:", s["experiment_winrate"],
        "| forward:", s["walk_forward"]["forward_winrate"]
    )