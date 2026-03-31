from adaptive_brain_engine import AdaptiveBrainEngine

engine = AdaptiveBrainEngine()

report = engine.adapt()

print()
print("=== PM40 ADAPTIVE BRAIN ===")
print()

for k, v in report.items():
    print(k, ":", v)

print()