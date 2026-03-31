# context_memory.py

class ContextMemory:
    def __init__(self):
        self.memory = {}

    def _key(self, impulse, volume, regime):
        i = round(impulse, 1)
        v = round(volume, 1)
        return f"{i}:{v}:{regime}"

    def record(self, impulse, volume, regime, outcome):
        key = self._key(impulse, volume, regime)

        if outcome == "LOSS":
            self.memory[key] = self.memory.get(key, 0) + 1
        elif outcome == "WIN":
            if key in self.memory:
                del self.memory[key]

    def penalty(self, impulse, volume, regime):
        key = self._key(impulse, volume, regime)
        return self.memory.get(key, 0)

    def decay(self):
        for k in list(self.memory.keys()):
            self.memory[k] -= 1
            if self.memory[k] <= 0:
                del self.memory[k]
