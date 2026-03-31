from meta_brain_v2 import MetaBrain

print()
print("=== PM40 META BRAIN V2 ===")
print()

brain = MetaBrain()

result = brain.get_signal(
    "strong trend market breakout with pullback"
)

for k, v in result.items():
    print(k, ":", v)