from description_builder import DescriptionBuilder


class MultiTFBuilder:

    def __init__(self):

        self.builder = DescriptionBuilder()

    def build(self, prices15, prices30, prices1h, volumes):

        # 🔥 FIX: правильні TF
        d15 = self.builder.build(prices15, volumes)
        d30 = self.builder.build(prices30, volumes)
        d1h = self.builder.build(prices1h, volumes)

        parts15 = d15.split()
        parts30 = d30.split()
        parts1h = d1h.split()

        trend15 = parts15[0]
        trend30 = parts30[0]
        trend1h = parts1h[0]

        structure = parts15[1]
        volume = parts15[2]
        regime = parts15[3]

        description = (
            f"15m_{trend15} "
            f"30m_{trend30} "
            f"1h_{trend1h} "
            f"{structure} "
            f"{volume} "
            f"{regime}"
        )

        return description