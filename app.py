import cv2
import time
import numpy as np

from src.face_detection import FaceDetector
from src.blink_detection import BlinkDetector
from src.signal_extraction import SignalExtractor
from src.heart_rate_estimation import HeartRateEstimator
from src.graph_generator import GraphGenerator
from src.health_predictor import HealthPredictor


face_detector = FaceDetector()
blink_detector = BlinkDetector()
signal_extractor = SignalExtractor()
heart_estimator = HeartRateEstimator()
graph_generator = GraphGenerator()
health_predictor = HealthPredictor()

camera = cv2.VideoCapture(0)

start_time = time.time()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900


while True:

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    faces = face_detector.detect_face(frame)

    bpm = 0
    frequency = 0
    eye_status = "UNKNOWN"

    face_preview = np.zeros(
        (180, 180, 3),
        dtype=np.uint8
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
        main_view_frame = frame.copy()

        blink_data = blink_detector.detect_blinks(
            frame,
            (x, y, w, h)
        )

        eye_tracking_frame = frame.copy()

        frame = main_view_frame

        eye_status = blink_data["eye_status"]

        signal_extractor.extract_signal(
            frame,
            (x, y, w, h)
        )

        signal = signal_extractor.get_signal()

        bpm = heart_estimator.estimate_bpm(signal)

        frequency = round(bpm / 60, 2)

        face_preview = eye_tracking_frame[
            y:y + h,
            x:x + w
        ].copy()

        break

    signal = signal_extractor.get_signal()

    graph_generator.generate_signal_graph(signal)
    graph_generator.generate_fft_graph(signal)

    elapsed_minutes = max(
        (time.time() - start_time) / 60,
        0.01
    )

    blink_rate = round(
        blink_detector.blink_count /
        elapsed_minutes,
        1
    )

    health_status = health_predictor.predict(
        bpm,
        blink_rate
    )

    dashboard = np.zeros(
        (WINDOW_HEIGHT, WINDOW_WIDTH, 3),
        dtype=np.uint8
    )

    dashboard[:] = (25, 25, 25)

    main_view = cv2.resize(
        frame,
        (800, 450)
    )

    dashboard[
        20:470,
        20:820
    ] = main_view

    if face_preview.size > 0:

        face_preview = cv2.resize(
            face_preview,
            (220, 180)
        )

        dashboard[
            40:220,
            850:1070
        ] = face_preview

    cv2.putText(
        dashboard,
        "EYE VIEW",
        (890, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        dashboard,
        "AI HEART RATE & BLINK MONITOR",
        (20, 520),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )

    cv2.putText(
        dashboard,
        f"Heart Rate : {bpm} BPM",
        (20, 570),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        dashboard,
        f"Frequency : {frequency} Hz",
        (20, 610),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.putText(
        dashboard,
        f"Blink Count : {blink_detector.blink_count}",
        (20, 650),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        dashboard,
        f"Blink Rate : {blink_rate}/min",
        (20, 690),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    color = (0, 255, 0)

    if eye_status == "CLOSED":
        color = (0, 0, 255)

    cv2.putText(
        dashboard,
        f"Eye Status : {eye_status}",
        (20, 730),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    cv2.putText(
        dashboard,
        f"Health : {health_status}",
        (20, 770),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    signal_graph = cv2.imread(
        "static/graphs/signal_graph.png"
    )

    if signal_graph is not None:

        signal_graph = cv2.resize(
            signal_graph,
            (500, 180)
        )

        dashboard[
            260:440,
            850:1350
        ] = signal_graph

    fft_graph = cv2.imread(
        "static/graphs/fft_graph.png"
    )

    if fft_graph is not None:

        fft_graph = cv2.resize(
            fft_graph,
            (500, 180)
        )

        dashboard[
            470:650,
            850:1350
        ] = fft_graph

    cv2.imshow(
        "AI Heart Rate & Blink Monitoring System",
        dashboard
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()