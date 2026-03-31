from strategy_discovery_engine import StrategyDiscoveryEngine


engine = StrategyDiscoveryEngine()

results = engine.discover()

print()
print("=== PM40 STRATEGY DISCOVERY ===")
print()

for r in results:

    print(
        r["pattern"],
        "| trades:", r["trades"],
        "| raw:", r["winrate"],
        "| adjusted:", r["adjusted_winrate"],
        "| status:", r["status"]
    )