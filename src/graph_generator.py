import os
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft


class GraphGenerator:

    def __init__(self):
        self.graph_folder = "static/graphs"

        os.makedirs(self.graph_folder, exist_ok=True)

    def generate_signal_graph(self, signal):

        if len(signal) < 5:
            return

        plt.figure(figsize=(6, 3))
        plt.plot(signal)
        plt.title("Heart Signal")
        plt.xlabel("Samples")
        plt.ylabel("Green Intensity")
        plt.tight_layout()

        plt.savefig(
            os.path.join(
                self.graph_folder,
                "signal_graph.png"
            )
        )

        plt.close()

    def generate_fft_graph(self, signal):

        if len(signal) < 50:
            return

        signal = np.array(signal)

        fft_values = np.abs(fft(signal))

        plt.figure(figsize=(6, 3))
        plt.plot(fft_values[:len(fft_values)//2])
        plt.title("FFT Spectrum")
        plt.xlabel("Frequency Bin")
        plt.ylabel("Magnitude")
        plt.tight_layout()

        plt.savefig(
            os.path.join(
                self.graph_folder,
                "fft_graph.png"
            )
        )

        plt.close()