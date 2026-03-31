import numpy as np

class TrendDetector:

    def detect(self, prices):

        if len(prices) < 10:
            return "sideways"

        short_ma = np.mean(prices[-5:])
        long_ma = np.mean(prices[-10:])

        if short_ma > long_ma:
            return "uptrend"

        if short_ma < long_ma:
            return "downtrend"

        return "sideways"