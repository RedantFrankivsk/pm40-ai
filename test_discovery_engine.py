from discovery_engine import DiscoveryEngine

engine = DiscoveryEngine()

patterns = engine.generate_patterns()

print()
print("=== PM40 DISCOVERY ENGINE ===")
print()

print("Generated patterns:", len(patterns))
print()

for p in patterns:

    print(p)

print()