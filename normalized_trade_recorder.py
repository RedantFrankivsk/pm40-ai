from pattern_memory import PatternMemory
from pattern_normalizer import PatternNormalizer


class NormalizedTradeRecorder:

    def __init__(self):

        self.memory = PatternMemory()
        self.normalizer = PatternNormalizer()

    def record(self, pattern, result):

        normalized = self.normalizer.normalize(pattern)

        win = False

        if result.upper() == "WIN":
            win = True

        self.memory.record_trade(normalized, win)

        print()
        print("Trade recorded")
        print("Original:", pattern)
        print("Normalized:", normalized)
        print("Result:", result)
        print()