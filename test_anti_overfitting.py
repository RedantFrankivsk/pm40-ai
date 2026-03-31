from anti_overfitting_engine import AntiOverfittingEngine


strategies = [

    {
        "pattern": ["breakout", "pullback", "trend_market"],
        "trades": 159,
        "winrate": 0.692
    },

    {
        "pattern": ["low_volume", "pullback", "trend_market"],
        "trades": 174,
        "winrate": 0.661
    },

    {
        "pattern": ["breakout", "low_volume", "range_market"],
        "trades": 88,
        "winrate": 0.727
    },

    {
        "pattern": ["normal_volume", "pullback", "range_market"],
        "trades": 30,
        "winrate": 0.72
    }

]


engine = AntiOverfittingEngine()

results = engine.filter_strategies(strategies)

print()
print("=== PM40 ANTI OVERFITTING TEST ===")
print()

for r in results:

    print(
        r["pattern"],
        "| trades:", r["trades"],
        "| raw:", r["winrate"],
        "| adjusted:", r["adjusted_winrate"],
        "| status:", r["status"]
    )