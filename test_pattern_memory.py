from pattern_memory_MARCH import PatternMemory


print()
print("=== PM40 PATTERN MEMORY TEST ===")
print()

pm = PatternMemory()


p1 = pm.add_pattern(
    "breakout after pullback with strong trend",
    {"market": "trend_market"}
)

p2 = pm.add_pattern(
    "low volume pullback continuation",
    {"market": "trend_market"}
)

p3 = pm.add_pattern(
    "range breakout with volatility spike",
    {"market": "range_market"}
)


pm.record_outcome(p1["id"], "win")
pm.record_outcome(p2["id"], "loss")
pm.record_outcome(p3["id"], "win")


patterns = pm.get_all()

for p in patterns:

    print(
        p["id"],
        "|",
        p["description"],
        "| conf:",
        p["confidence"],
        "| wins:",
        p["wins"],
        "| losses:",
        p["losses"]
    )