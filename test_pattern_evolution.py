from pattern_evolution_engine import PatternEvolutionEngine


engine = PatternEvolutionEngine()

base_pattern = "normal_volume pullback trend_market"

results = engine.evolve(base_pattern)


print("\n=== EVOLUTION RESULTS ===\n")

for r in results:

    print(
        r["pattern"],
        "| trades:", r["trades"],
        "| winrate:", r["winrate"],
        "| score:", r["score"]
    )