from meta_learning_engine import MetaLearningEngine

engine = MetaLearningEngine()

pattern_stats = engine.pattern_stats()
strategy_stats = engine.strategy_stats()
regime_stats = engine.regime_stats()

print()
print("=== META LEARNING ===")
print()

print("PATTERN PERFORMANCE")
print()

for p in pattern_stats:

    print(
        p["pattern"],
        "| trades:", p["trades"],
        "| wins:", p["wins"],
        "| winrate:", round(p["winrate"], 3)
    )

print()

print("STRATEGY PERFORMANCE")
print()

for s in strategy_stats:

    print(
        s["strategy"],
        "| trades:", s["trades"],
        "| wins:", s["wins"],
        "| winrate:", round(s["winrate"], 3)
    )

print()

print("REGIME PERFORMANCE")
print()

for r in regime_stats:

    print(
        r["regime"],
        "| trades:", r["trades"],
        "| wins:", r["wins"],
        "| winrate:", round(r["winrate"], 3)
    )

print()