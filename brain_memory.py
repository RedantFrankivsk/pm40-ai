import json
import os
import time


class BrainMemory:

    def __init__(self):

        self.file = "brain_memory.json"

        if not os.path.exists(self.file):
            self.memory = []
            self.save()
        else:
            with open(self.file, "r") as f:
                self.memory = json.load(f)

    def save(self):

        with open(self.file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def record_signal(self, brain_name, pattern, signal):

        trade = {

            "brain": brain_name,
            "pattern": pattern,
            "signal": signal,
            "result": None,
            "timestamp": int(time.time())
        }

        self.memory.append(trade)

        self.save()

        return trade

    def record_result(self, index, result):

        if index >= len(self.memory):
            return

        self.memory[index]["result"] = result

        self.save()

    def get_brain_stats(self, brain_name):

        wins = 0
        losses = 0

        for t in self.memory:

            if t["brain"] != brain_name:
                continue

            if t["result"] == "win":
                wins += 1

            if t["result"] == "loss":
                losses += 1

        total = wins + losses

        if total == 0:
            winrate = 0

        else:
            winrate = wins / total

        return {

            "wins": wins,
            "losses": losses,
            "winrate": round(winrate, 3)
        }

    def get_all(self):

        return self.memory