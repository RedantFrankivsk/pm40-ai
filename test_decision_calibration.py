from decision_calibration_engine import DecisionCalibrationEngine

engine = DecisionCalibrationEngine()

report = engine.calibration_report()

print()
print("=== DECISION CALIBRATION ===")
print()

print("High confidence trades:", report["high_conf_trades"])
print("High confidence winrate:", round(report["high_conf_winrate"], 3))

print()

print("Low confidence trades:", report["low_conf_trades"])
print("Low confidence winrate:", round(report["low_conf_winrate"], 3))

print()

print("Brain status:", report["status"])

print()