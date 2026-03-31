from strategy_execution_engine import StrategyExecutionEngine
from structure_detector import detect_structure
from structural_edge_engine import StructuralEdgeEngine


class ExecutionOptimizer:

    def __init__(self, outcome_memory):

        self.strategy_engine = StrategyExecutionEngine()
        self.edge_engine = StructuralEdgeEngine()
        self.memory = outcome_memory

        self.delay_required = False
        self.delay_counter = 0
        self.delay_steps = 1

        self.force_entry_counter = 0
        self.force_every = 2  # 🔥 БУЛО 3 → частіше

    def micro_structure_filter(self, candles, signal):

        structure = detect_structure(candles)
        trend = structure.get("trend", "FLAT")

        if signal == "UP" and trend == "DOWN":
            return False

        if signal == "DOWN" and trend == "UP":
            return False

        return True

    def structural_edge_filter(self, pattern):

        edges = self.edge_engine.discover()

        if not edges:
            return None

        for e in edges:
            if e["structure"] in pattern:

                if e["winrate"] < 0.45:  # 🔥 БУЛО 0.5
                    return False

                return True

        return None

    def timing_filter(self):

        # 🔥 ПОСЛАБЛЕНО
        if not self.delay_required:
            self.delay_required = True
            self.delay_counter = 0
            return True  # 🔥 БУЛО False

        self.delay_counter += 1

        if self.delay_counter >= self.delay_steps:
            self.delay_required = False
            return True

        return True  # 🔥 НЕ блокуємо

    def outcome_filter(self):

        try:
            if self.memory.should_block():
                return False
        except:
            pass

        return True

    def force_entry_logic(self):

        self.force_entry_counter += 1

        if self.force_entry_counter >= self.force_every:
            self.force_entry_counter = 0
            return True

        return False

    def should_execute(self, pattern, candles, signal):

        print("\n=== EXECUTION OPTIMIZER ===")

        if not self.outcome_filter():
            return False

        strategy_ok = self.strategy_engine.should_trade(pattern)

        if not strategy_ok:
            if not self.force_entry_logic():
                print("[EXECUTION] soft block (strategy)")
                return False
            else:
                print("[EXECUTION] FORCE bypass strategy")

        if not self.micro_structure_filter(candles, signal):
            return False

        edge_state = self.structural_edge_filter(pattern)

        # 🔥 ГОЛОВНИЙ ФІКС
        if edge_state is False:
            return False

        if edge_state is None:
            print("[EDGE] no edge yet → allow learning")
            return True  # 🔥 БУЛО блокування

        if not self.timing_filter():
            return False

        return True