import os
import json

from strategy_discovery_engine import StrategyDiscoveryEngine
from strategy_generator import StrategyGenerator
from strategy_auto_evolution_engine import StrategyAutoEvolutionEngine
from strategy_execution_engine import StrategyExecutionEngine
from anti_overfitting_engine import AntiOverfittingEngine


class StrategyPipeline:

    def __init__(self):

        self.discovery = StrategyDiscoveryEngine()
        self.generator = StrategyGenerator()
        self.evolution = StrategyAutoEvolutionEngine()
        self.anti_overfit = AntiOverfittingEngine()

        self.execution = None

        self.discovery_file = "strategy_discovery.json"
        self.filtered_file = "strategy_filtered.json"
        self.auto_file = "auto_strategies.json"

    # =========================
    # STEP 1 — DISCOVERY
    # =========================
    def run_discovery(self):

        print("\n[PIPELINE] STEP 1: Discovery")

        strategies = self.discovery.run()

        print(f"[PIPELINE] Found {len(strategies)} raw strategies")

        return strategies

    # =========================
    # STEP 2 — ANTI OVERFITTING
    # =========================
    def run_anti_overfit(self):

        print("\n[PIPELINE] STEP 2: Anti-Overfitting")

        strategies = self.anti_overfit.run()

        print(f"[PIPELINE] Filtered to {len(strategies)} strategies")

        return strategies

    # =========================
    # STEP 3 — GENERATOR
    # =========================
    def run_generator(self):

        print("\n[PIPELINE] STEP 3: Generator")

        strategies = self.generator.build()

        print(f"[PIPELINE] Generated {len(strategies)} strong strategies")

        return strategies

    # =========================
    # STEP 4 — AUTO EVOLUTION
    # =========================
    def run_evolution(self):

        print("\n[PIPELINE] STEP 4: Evolution")

        strategies = self.evolution.evolve()

        self.evolution.save(strategies)

        print(f"[PIPELINE] Evolved {len(strategies)} elite strategies")

        return strategies

    # =========================
    # STEP 5 — LOAD EXECUTION
    # =========================
    def load_execution(self):

        print("\n[PIPELINE] STEP 5: Execution Engine")

        self.execution = StrategyExecutionEngine()

    # =========================
    # FULL PIPELINE
    # =========================
    def run_full_cycle(self):

        print("\n========== STRATEGY PIPELINE START ==========")

        self.run_discovery()
        self.run_anti_overfit()
        self.run_generator()
        self.run_evolution()
        self.load_execution()

        print("\n========== STRATEGY PIPELINE READY ==========\n")

    # =========================
    # ENTRY FILTER
    # =========================
    def should_trade(self, description):

        if not self.execution:
            self.load_execution()

        decision = self.execution.should_trade(description)

        if decision:
            print("[PIPELINE] ✅ Strategy APPROVED trade")
        else:
            print("[PIPELINE] ❌ Strategy BLOCKED trade")

        return decision

    # =========================
    # DEBUG EXPLAIN
    # =========================
    def explain(self, description):

        if not self.execution:
            self.load_execution()

        explanation = self.execution.explain(description)

        if explanation:
            print("[PIPELINE] MATCHED STRATEGY:")
            print(explanation)
        else:
            print("[PIPELINE] No strategy match")

        return explanation