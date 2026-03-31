from regime_committee import RegimeCommittee
from market_simulator import MarketSimulator


committee = RegimeCommittee()
market = MarketSimulator()

print()
print("=== PM40 REGIME COMMITTEE TEST ===")
print()

for i in range(20):

    m = market.generate_market_for_pattern({
        "pattern": ["breakout", "pullback", "trend_market"]
    })

    decision = committee.decide(
        m["pattern"],
        m["context"],
        m["regime"]
    )

    print(
        m["pattern"],
        "| regime:", m["regime"],
        "| signal:", decision["final_signal"]
    )