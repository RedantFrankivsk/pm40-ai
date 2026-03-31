from pattern_analyzer import PatternAnalyzer


analyzer = PatternAnalyzer()

print("\n=== STRONG PATTERNS ===")

for p in analyzer.strongest_patterns():

    print(
        p["pattern"],
        "| trades:", p["total"],
        "| winrate:", round(p["winrate"] * 100, 2), "%"
    )


print("\n=== WEAK PATTERNS ===")

for p in analyzer.weakest_patterns():

    print(
        p["pattern"],
        "| trades:", p["total"],
        "| winrate:", round(p["winrate"] * 100, 2), "%"
    )