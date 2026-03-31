from pattern_memory import PatternMemory
from pattern_normalizer import PatternNormalizer
from pattern_expansion_engine import PatternExpansionEngine


class ExpandedTradeRecorder:

    def __init__(self):

        self.memory = PatternMemory()
        self.normalizer = PatternNormalizer()
        self.expander = PatternExpansionEngine()

    def record(self, pattern, result):

        normalized = self.normalizer.normalize(pattern)

        expansions = self.expander.expand(normalized)

        win = False

        if result.upper() == "WIN":
            win = True

        for p in expansions:

            self.memory.record_trade(p, win)

        print()
        print("Trade recorded")
        print("Original:", pattern)
        print("Normalized:", normalized)
        print("Expansions:", len(expansions))
        print("Result:", result)
        print()