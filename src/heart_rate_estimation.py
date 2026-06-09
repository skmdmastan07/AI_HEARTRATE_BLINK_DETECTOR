import numpy as np
from scipy.fft import fft


class HeartRateEstimator:
    def __init__(self):
        self.fps = 30

    def estimate_bpm(self, signal):

        if len(signal) < 150:
            return 0

        signal = np.array(signal)

        signal = signal - np.mean(signal)

        fft_values = np.abs(fft(signal))

        frequencies = np.fft.fftfreq(
            len(signal),
            d=1 / self.fps
        )

        valid = np.where(
            (frequencies >= 0.8) &
            (frequencies <= 3.0)
        )

        if len(valid[0]) == 0:
            return 0

        peak_freq = frequencies[valid][
            np.argmax(fft_values[valid])
        ]

        bpm = peak_freq * 60

        return round(float(bpm), 1)