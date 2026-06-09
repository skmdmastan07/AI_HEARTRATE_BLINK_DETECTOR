import numpy as np


class SignalExtractor:
    def __init__(self):
        self.signal_buffer = []

    def extract_signal(self, frame, face):
        x, y, w, h = face

        forehead_y1 = y + int(h * 0.1)
        forehead_y2 = y + int(h * 0.25)

        forehead_x1 = x + int(w * 0.25)
        forehead_x2 = x + int(w * 0.75)

        forehead = frame[
            forehead_y1:forehead_y2,
            forehead_x1:forehead_x2
        ]

        if forehead.size == 0:
            return None

        green_mean = np.mean(forehead[:, :, 1])

        self.signal_buffer.append(green_mean)

        if len(self.signal_buffer) > 300:
            self.signal_buffer.pop(0)

        return green_mean

    def get_signal(self):
        return self.signal_buffer