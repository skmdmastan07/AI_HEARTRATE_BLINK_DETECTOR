import cv2


class BlinkDetector:
    def __init__(self):
        self.eye_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye.xml"
        )

        self.blink_count = 0
        self.eye_closed_frames = 0
        self.blink_detected = False
        self.eye_status = "OPEN"

    def detect_blinks(self, frame, face):

        x, y, w, h = face

        roi = frame[y:y + h, x:x + w]

        gray_roi = cv2.cvtColor(
            roi,
            cv2.COLOR_BGR2GRAY
        )

        eyes = self.eye_cascade.detectMultiScale(
            gray_roi,
            scaleFactor=1.1,
            minNeighbors=5
        )

        eye_count = len(eyes)

        if eye_count < 2:

            self.eye_status = "CLOSED"

            self.eye_closed_frames += 1

        else:

            self.eye_status = "OPEN"

            if (
                self.eye_closed_frames >= 1
                and not self.blink_detected
            ):
                self.blink_count += 1
                self.blink_detected = True

            self.eye_closed_frames = 0

        if eye_count >= 2:
            self.blink_detected = False

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(
                roi,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )

        return {
            "blink_count": self.blink_count,
            "eye_status": self.eye_status,
            "eye_count": eye_count
        }