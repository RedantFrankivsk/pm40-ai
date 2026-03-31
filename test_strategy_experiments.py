from strategy_experiment_engine import StrategyExperimentEngine

engine = StrategyExperimentEngine()

results = engine.run()

print()
print("=== PM40 STRATEGY EXPERIMENTS ===")
print()

for k, v in results.items():

    trades = v.get("trades", 0)
    wins = v.get("wins", 0)

    if trades > 0:
        winrate = wins / trades
    else:
        winrate = 0

    print(
        v["pattern"],
        "| trades:", trades,
        "| wins:", wins,
        "| winrate:", round(winrate, 3),
        "| status:", v["status"]
    )

print()