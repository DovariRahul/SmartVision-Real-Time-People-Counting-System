🧠 SmartVision: Real-Time AI-Based People Counting System
📌 Project Overview

SmartVision is a real-time people counting and occupancy monitoring system developed using computer vision and deep learning techniques. The system detects, tracks, and counts the number of people present in a room or monitored area using a live camera feed or video input.

The project is designed to provide accurate, real-time occupancy estimation, making it suitable for applications such as smart buildings, classrooms, offices, malls, and security systems.

🎯 Objectives

Detect people accurately in real-time video streams

Track individuals uniquely even during movement and partial occlusion

Count the number of people currently present in a room

Ensure real-time performance with minimal latency

Build a robust and scalable computer vision system

🚀 Key Features

Real-time people detection using deep learning

Multi-object tracking with unique ID assignment

Accurate room occupancy counting

Fullscreen live video display

FPS (Frames Per Second) performance monitoring

Robust against lighting changes and movement

🛠 Tools and Technologies Used
🔹 Programming Language

Python 3

🔹 Computer Vision

OpenCV – video capture, frame processing, visualization

🔹 Deep Learning

YOLOv8 (You Only Look Once) – real-time people detection

Ultralytics YOLO Framework

🔹 Object Tracking

SORT (Simple Online and Realtime Tracking)

Kalman Filter for motion prediction

Hungarian Algorithm for data association

🔹 Background Processing (Optional)

MOG2 Background Subtraction

🔹 Supporting Libraries

NumPy – numerical computations

SciPy – scientific computing

FilterPy – Kalman filtering

PyYAML – configuration management

scikit-image – SORT dependency

🏗 System Architecture

Video Input

Live camera feed or pre-recorded video

Object Detection

YOLO detects people in each frame

Object Tracking

SORT assigns and maintains unique IDs

Occupancy Counting

Active tracked IDs represent people currently in the room

Visualization

Bounding boxes, IDs, occupancy count, and FPS displayed

📂 Project Structure
RealTime_Object_Counting/
│
├── main.py
├── README.md
├── requirements.txt
│
├── config/
│   └── config.yaml
│
├── models/
│   └── yolo/
│       └── yolov8n.pt
│
├── src/
│   ├── app/
│   │   └── pipeline.py
│   ├── detection/
│   │   └── yolo_detector.py
│   ├── tracking/
│   │   ├── sort.py
│   │   └── sort_tracker.py
│   ├── counting/
│   │   └── occupancy_counter.py
│   └── utils/
│       ├── visualization.py
│       └── fps.py
│
└── data/
    └── videos/

▶️ How to Run the Project
1️⃣ Install Required Libraries
pip install -r requirements.txt

2️⃣ Run the Application
python main.py

3️⃣ Controls

Press ESC or q to stop the video stream

📊 Performance

Real-time processing at 15–30 FPS (depending on hardware)

Accurate tracking and stable occupancy count

Optimized for CPU-based execution (GPU optional)

📌 Applications

Smart classrooms and lecture halls

Office occupancy monitoring
Shopping malls and public spaces

Security and surveillance systems

Smart building automation

🧾 Conclusion

SmartVision demonstrates the effective use of deep learning and computer vision techniques for real-time people counting and occupancy monitoring. The system is modular, extensible, and suitable for both academic and real-world applications.
