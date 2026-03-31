from genetic_evolution_engine import GeneticEvolutionEngine


print()
print("=== PM40 GENETIC EVOLUTION ===")
print()

engine = GeneticEvolutionEngine()

brains = engine.evolve()

if not brains:

    print("No new genetic brains")

else:

    for b in brains:

        print(
            b["name"],
            "| forward:", b["forward_winrate"]
        )