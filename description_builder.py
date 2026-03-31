from trend_detector import TrendDetector
from structure_detector import StructureDetector
from volume_detector import VolumeDetector
from market_regime_detector import MarketRegimeDetector


class DescriptionBuilder:

    def __init__(self):

        self.trend = TrendDetector()
        self.structure = StructureDetector()
        self.volume = VolumeDetector()
        self.regime = MarketRegimeDetector()

    def build(self, prices, volumes):

        trend = self.trend.detect(prices)

        structure = self.structure.detect(prices)

        volume = self.volume.detect(volumes)

        regime = self.regime.detect(prices)

        description = f"{trend} {structure} {volume} {regime}"

        return description