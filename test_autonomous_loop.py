from autonomous_research_loop import AutonomousResearchLoop

loop = AutonomousResearchLoop()

report = loop.run_cycle()

print()
print("=== PM40 AUTONOMOUS RESEARCH LOOP ===")
print()

print("Strongest patterns:")

for p in report["strongest_patterns"]:

    print(
        p["pattern"],
        "| trades:", p["trades"],
        "| winrate:", round(p["winrate"], 3),
        "| strength:", round(p["strength"], 3)
    )

print()

print("New strategies created:", len(report["new_strategies"]))

for s in report["new_strategies"]:

    print(
        s["pattern"],
        "| direction:", s["direction"],
        "| risk:", s["risk"]
    )

print()

brain = report["brain_status"]

print("Brain calibration status:", brain["status"])

print()