import numpy as np


class MarketRegimeDetector:

    def detect(self, prices):

        if len(prices) < 20:
            return "normal_market"

        returns = []

        for i in range(1, len(prices)):
            returns.append(prices[i] - prices[i-1])

        volatility = np.std(returns)

        move = abs(prices[-1] - prices[0])

        if volatility > 0.9:
            return "volatile_market"

        if move > 3:
            return "trend_market"

        return "range_market"