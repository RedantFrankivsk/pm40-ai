import json
import os
from datetime import datetime, timezone


class RiskManager:

    def __init__(self):

        self.file = "risk_state.json"

        self.base_bet = 1.0

        self.max_loss_streak = 3
        self.max_daily_loss = -5
        self.max_daily_profit = 10

        self.load()

    def now(self):
        return datetime.now(timezone.utc)

    def load(self):

        if not os.path.exists(self.file):

            self.state = {
                "balance": 100.0,
                "start_balance": 100.0,
                "loss_streak": 0,
                "daily_pnl": 0,
                "last_trade_time": None
            }

            self.save()
            return

        with open(self.file, "r") as f:
            self.state = json.load(f)

        # 🔥 FIX: якщо файл битий або пустий
        if "loss_streak" not in self.state:
            self.state["loss_streak"] = 0

        if "daily_pnl" not in self.state:
            self.state["daily_pnl"] = 0

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.state, f, indent=4)

    # =========================
    # AUTO RESET (🔥 КЛЮЧ)
    # =========================
    def auto_reset_if_stuck(self):

        # якщо нема жодного трейду → не блокуємо
        if self.state.get("last_trade_time") is None:
            self.state["loss_streak"] = 0
            return

        try:
            last = datetime.fromisoformat(self.state["last_trade_time"])
            if last.tzinfo is None:
                last = last.replace(tzinfo=timezone.utc)
        except:
            self.state["loss_streak"] = 0
            return

        minutes = (self.now() - last).total_seconds() / 60

        # 🔥 якщо довго не було трейдів → reset
        if minutes > 60:
            print("[RISK] auto reset loss streak (timeout)")
            self.state["loss_streak"] = 0

    # =========================
    # UPDATE
    # =========================
    def update_after_trade(self, result):

        self.state["last_trade_time"] = self.now().isoformat()

        if result == "WIN":
            profit = self.base_bet * 0.8
            self.state["balance"] += profit
            self.state["daily_pnl"] += profit
            self.state["loss_streak"] = 0

        elif result == "LOSS":
            loss = self.base_bet
            self.state["balance"] -= loss
            self.state["daily_pnl"] -= loss
            self.state["loss_streak"] += 1

        self.save()

    # =========================
    # CAN TRADE (🔥 FIXED)
    # =========================
    def can_trade(self):

        self.auto_reset_if_stuck()

        # 🔥 якщо нема історії — дозволяємо
        if self.state.get("last_trade_time") is None:
            return True, "LEARNING MODE"

        if self.state["loss_streak"] >= self.max_loss_streak:
            return False, "LOSS STREAK LIMIT"

        if self.state["daily_pnl"] <= self.max_daily_loss:
            return False, "DAILY LOSS LIMIT"

        if self.state["daily_pnl"] >= self.max_daily_profit:
            return False, "DAILY PROFIT TARGET"

        return True, "OK"

    def get_bet_size(self, confidence):

        if confidence >= 80:
            return self.base_bet * 1.5

        if confidence >= 60:
            return self.base_bet * 1.0

        return self.base_bet * 0.5