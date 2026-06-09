AI-Based Contactless Heart Rate and Eye Blink Monitoring System

Overview

This project is a real-time computer vision application that estimates heart rate and monitors eye blinks using a webcam. The system uses OpenCV-based face and eye detection, signal processing techniques, FFT analysis, and a professional dashboard interface to display health-related metrics in real time.

The application works without any external medical devices and demonstrates contactless monitoring using a standard webcam.

Features

- Real-time webcam monitoring
- Face detection using OpenCV Haar Cascades
- Eye detection and blink counting
- Eye status detection (Open / Closed)
- Blink rate calculation
- Forehead ROI extraction
- Green channel signal extraction
- Heart rate estimation using FFT
- Frequency calculation
- Real-time signal graph
- Real-time FFT graph
- Professional OpenCV dashboard
- Face view and eye view panels

Project Structure

AI_HEARTRATE_BLINK_DETECTOR/

├── dataset/
├── models/
│   └── heart_rate_model.pkl
├── src/
│   ├── __init__.py
│   ├── face_detection.py
│   ├── blink_detection.py
│   ├── signal_extraction.py
│   ├── heart_rate_estimation.py
│   ├── graph_generator.py
│   └── health_predictor.py
├── static/
│   └── graphs/
├── app.py
├── requirements.txt
└── README.md

Installation

1. Clone the repository


2. Move into the project folder

cd AI_HEARTRATE_BLINK_DETECTOR

3. Install dependencies

pip install -r requirements.txt

How to Run

Run the application using:

python app.py

A desktop OpenCV dashboard window will open automatically.

Controls

- Press ESC to close the application.
- Ensure a webcam is connected before starting the project.

Displayed Metrics

- Heart Rate (BPM)
- Signal Frequency (Hz)
- Blink Count
- Blink Rate
- Eye Status (OPEN / CLOSED)

Technologies Used

- Python
- OpenCV
- NumPy
- SciPy
- Matplotlib
- Scikit-Learn

Note

This project is developed for educational and academic purposes only. The displayed heart rate values are approximate estimates and should not be used for medical diagnosis.

Author 
Mastan Vali