# test_pattern_compression.py

from pattern_compression_engine import PatternCompressionEngine


engine = PatternCompressionEngine()

pattern = "normal_volume pullback trend_market session_london"

results = engine.evaluate(pattern)

print("\n=== COMPRESSION RESULTS ===\n")

for r in results[:10]:

    print(
        r["pattern"],
        "| trades:", r["trades"],
        "| winrate:", round(r["winrate"], 3),
        "| score:", round(r["score"], 4)
    )