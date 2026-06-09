class HealthPredictor:

    def predict(self, bpm, blink_rate):

        if bpm == 0:
            return "Analyzing..."

        if 60 <= bpm <= 100 and blink_rate <= 25:
            return "Normal"

        if bpm < 60:
            return "Low Heart Rate"

        if bpm > 100:
            return "Elevated Heart Rate"

        return "Attention Needed"