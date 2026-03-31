import json


class DecisionCalibrationEngine:

    def __init__(self):

        self.file = "experience_memory.json"

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def calibration_stats(self):

        data = self.load()

        high_conf_trades = 0
        high_conf_wins = 0

        low_conf_trades = 0
        low_conf_wins = 0

        for e in data:

            conf = e.get("confidence", 0.5)

            if conf >= 0.7:

                high_conf_trades += 1

                if e["result"] == "WIN":
                    high_conf_wins += 1

            if conf <= 0.4:

                low_conf_trades += 1

                if e["result"] == "WIN":
                    low_conf_wins += 1

        high_wr = high_conf_wins / high_conf_trades if high_conf_trades > 0 else 0
        low_wr = low_conf_wins / low_conf_trades if low_conf_trades > 0 else 0

        return {
            "high_conf_trades": high_conf_trades,
            "high_conf_winrate": high_wr,
            "low_conf_trades": low_conf_trades,
            "low_conf_winrate": low_wr
        }

    def calibration_report(self):

        stats = self.calibration_stats()

        report = {}

        report["high_conf_trades"] = stats["high_conf_trades"]
        report["high_conf_winrate"] = stats["high_conf_winrate"]

        report["low_conf_trades"] = stats["low_conf_trades"]
        report["low_conf_winrate"] = stats["low_conf_winrate"]

        if stats["high_conf_winrate"] < 0.55:
            report["status"] = "OVERCONFIDENT"

        elif stats["low_conf_winrate"] > 0.55:
            report["status"] = "UNDERCONFIDENT"

        else:
            report["status"] = "CALIBRATED"

        return report