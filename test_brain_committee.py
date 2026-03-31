from brain_committee import BrainCommittee

committee = BrainCommittee()

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

result = committee.decide(
    pattern,
    context,
    "trend_market"
)

print()
print("=== PM40 BRAIN COMMITTEE ===")
print()

print("FINAL SIGNAL:", result["final_signal"])
print()

for vote in result["votes"]:

    print(
        vote["brain"],
        "| signal:", vote["signal"],
        "| confidence:", vote["confidence"]
    )

print()