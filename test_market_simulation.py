from market_simulation_engine import MarketSimulationEngine

engine = MarketSimulationEngine()

trades = engine.run_simulation(10)

print()
print("=== PM40 MARKET SIMULATION ===")
print()

for t in trades:

    print(
        "pattern:", t["pattern"],
        "| context:", t["context"],
        "| regime:", t["regime"],
        "| result:", t["result"]
    )

print()