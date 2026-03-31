from pattern_memory import PatternMemory


class TradeRecorder:

    def __init__(self):

        self.memory = PatternMemory()

    def record(self, pattern, result):

        win = False

        if result.upper() == "WIN":
            win = True

        self.memory.record_trade(pattern, win)

        print()
        print("Trade recorded:")
        print(pattern)
        print("Result:", result)
        print()