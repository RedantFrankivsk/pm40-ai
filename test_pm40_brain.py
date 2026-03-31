from pm40_brain import PM40Brain

brain = PM40Brain()

pattern = [
    "normal_volume",
    "pullback",
    "trend_market"
]

context = [
    "session_london",
    "volatility_normal",
    "strong_trend"
]

result = brain.analyze(pattern, context)

print()
print("=== PM40 BRAIN ANALYSIS ===")
print()

print("Signal:", result["signal"])
print("Regime:", result["regime"])
print("Strategy:", result["strategy"])

print()