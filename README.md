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
## Requirements
```
ultralytics==8.1.24
opencv-python==4.9.0.80
cvzone==1.5.6
numpy==1.26.4
torch==2.2.2+cu126
torchvision==0.17.2+cu126
```
## ✅ Steps to Run the Project

### 1️⃣ Download or Clone the Repository

```bash
git clone https://github.com/Pratheek-Poojary23/Vehicle-Detection-and-Counting-System-using-YOLOv11-using-opencv.git
cd Vehicle-Detection-and-Counting-System-using-YOLOv11-using-opencv
```

### Run the Python Script
```bash
python car_counter.py
```
## 📈 Result Demo

[![Click to view demo](https://github.com/Pratheek-Poojary23/Vehicle-Detection-and-Counting-System-using-YOLOv11-using-opencv/blob/main/video/preview.png)](https://github.com/Pratheek-Poojary23/Vehicle-Detection-and-Counting-System-using-YOLOv11-using-opencv/blob/main/counted_output.mp4)

> 🔗 Click the image above to view the output demo video.
