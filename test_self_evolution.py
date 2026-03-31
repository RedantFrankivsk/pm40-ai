from self_evolution_engine import SelfEvolutionEngine

engine = SelfEvolutionEngine()

new_strategies = engine.evolve()

print()
print("=== SELF EVOLUTION ===")
print()

print("New strategies created:", len(new_strategies))
print()

for s in new_strategies:

    print(
        s["pattern"],
        "| direction:", s["direction"],
        "| risk:", s["risk"]
    )

print()