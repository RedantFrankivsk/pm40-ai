import numpy as np

class VolumeDetector:

    def detect(self, volumes):

        if len(volumes) < 10:
            return "normal_volume"

        avg = np.mean(volumes[:-1])
        current = volumes[-1]

        if current > avg * 1.5:
            return "high_volume"

        if current < avg * 0.7:
            return "low_volume"

        return "normal_volume"