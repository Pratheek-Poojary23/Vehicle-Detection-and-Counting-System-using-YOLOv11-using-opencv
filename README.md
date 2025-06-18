# Vehicle Detection and Counting System using YOLOv11

This project implements a **real-time vehicle detection and counting system** using the [YOLOv11](https://github.com/ultralytics/ultralytics) object detection model. It uses OpenCV and SORT tracking to detect and count cars, buses, trucks, and motorbikes from a video source, with real-time annotation and ID tracking.

## 🔍 Features

- 🚗 Vehicle detection using YOLOv11
- 🔢 Unique vehicle ID assignment and counting
- 📈 Region-of-interest (ROI) based count validation
- 🖼 Overlay graphics and visual tracking using cvzone
- 🧠 SORT tracker for accurate object tracking
- ✅ CUDA acceleration for fast processing

---

## 📂 Project Structure

```
├── car_counter.py       # Main Python script for detection and counting
├── yolo11n.pt           # YOLOv11 model weights (should be downloaded separately)
├── sort.py              # SORT tracking module
├── mask.png             # Region mask to focus on area of interest
├── graphics.png         # Overlay graphics for UI
├── /videos/cars.mp4     # Input video file
├── counted_output.mp4   # [Optional] Output video with visualized detections
└── README.md            # This file
```
