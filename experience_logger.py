# =========================
# EXPERIENCE LOGGER (CLEAN FIX v2)
# =========================

import json
import os
from datetime import datetime


class ExperienceLogger:

    def __init__(self, file="experience_memory.json"):
        self.file = file

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def load(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    # =========================
    # MAIN LOG ONLY (NO PATTERN MEMORY HERE)
    # =========================
    def log_trade(self, symbol, signal, result, pattern, strategy_pattern, regime):

        data = self.load()

        data.append({
            "time": datetime.utcnow().isoformat(),
            "symbol": symbol,
            "signal": signal,
            "result": result,
            "pattern": str(pattern),
            "strategy_pattern": strategy_pattern,
            "regime": regime
        })

        self.save(data)