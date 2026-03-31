from strategy_genome_engine import StrategyGenomeEngine

engine = StrategyGenomeEngine()

genomes = engine.run()

print()
print("=== STRATEGY GENOMES ===")
print()

for g in genomes:

    print(
        "pattern:", g["entry_pattern"],
        "| direction:", g["direction"],
        "| risk:", g["risk_model"],
        "| confidence:", g["confidence"]
    )

print()