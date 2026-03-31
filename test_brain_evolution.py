from brain_evolution_engine import BrainEvolutionEngine


print()
print("=== PM40 BRAIN EVOLUTION ===")
print()

engine = BrainEvolutionEngine()

new_brains = engine.evolve()

if not new_brains:

    print("No new brains created")

else:

    for b in new_brains:

        print(
            b["name"],
            "| experiment:", b["experiment_winrate"],
            "| forward:", b["forward_winrate"]
        )