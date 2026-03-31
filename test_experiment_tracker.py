from experiment_tracker import ExperimentTracker

tracker = ExperimentTracker()

trade = {

    "pattern": "normal_volume pullback trend_market",
    "direction": "reversal",
    "result": "win"
}

tracker.update(trade)

print()
print("=== EXPERIMENT TRACKED ===")
print()
print("trade recorded")
print()