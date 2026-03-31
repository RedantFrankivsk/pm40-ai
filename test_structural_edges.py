from structural_edge_engine import StructuralEdgeEngine

engine = StructuralEdgeEngine()

edges = engine.discover()

print()
print("=== STRUCTURAL EDGES ===")
print()

for e in edges:

    print(
        e["structure"],
        "| trades:", e["trades"],
        "| winrate:", e["winrate"],
        "| score:", e["score"]
    )

print()