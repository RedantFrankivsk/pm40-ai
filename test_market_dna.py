from market_dna_engine import MarketDNAEngine

engine = MarketDNAEngine()

dna = engine.build_map()

print()
print("=== MARKET DNA MAP ===")
print()

for d in dna:

    print(
        d["pattern"],
        "| trades:", d["trades"],
        "| winrate:", d["winrate"],
        "| score:", d["score"]
    )

print()