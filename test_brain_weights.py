from brain_weighting_engine import BrainWeightingEngine

engine = BrainWeightingEngine()

sample_trades = [

    {"brain": "TrendBrain", "result": "win"},
    {"brain": "TrendBrain", "result": "win"},
    {"brain": "TrendBrain", "result": "loss"},
    {"brain": "TrendBrain", "result": "win"},
    {"brain": "TrendBrain", "result": "win"},

    {"brain": "ReversalBrain", "result": "loss"},
    {"brain": "ReversalBrain", "result": "loss"},
    {"brain": "ReversalBrain", "result": "win"},
    {"brain": "ReversalBrain", "result": "loss"},
    {"brain": "ReversalBrain", "result": "loss"}

]

weights = engine.update(sample_trades)

print()
print("=== PM40 BRAIN WEIGHTS ===")
print()

for k, v in weights.items():
    print(k, "weight:", v)

print()