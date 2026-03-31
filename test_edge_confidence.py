from edge_confidence_engine import EdgeConfidenceEngine

engine = EdgeConfidenceEngine()

edges = engine.analyze()

print()
print("=== EDGE CONFIDENCE ===")
print()

for e in edges:

    print(
        e["pattern"],
        "| trades:", e["trades"],
        "| winrate:", e["winrate"],
        "| score:", e["score"],
        "| confidence:", e["confidence"]
    )

print()