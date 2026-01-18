# Detection with YOLOv8 World

Welcome to this beginner-friendly **Object Detection** project using **YOLOv8 World** !
This project detect **objects in a video file or live camera feed**, draws bounding boxes with labels and saves the annotated output video. Simple, powerful and perfect for learning modern object detection.

---

## Prerequisites ✅

Before getting started, make sure you have:

- 🐍 **Python 3.8+**
- A **video file** (e.g., `cars.mp4`) or a **webcam`
- A code editor like **VS Code**

---

## Folder Structure 📂

Organize your project like this:

```
object-detection-using-yolo-world
├── detect.py                     # Main detection script
├── cars.mp4                      # Input video file (optional)
├── yolov8m-world.pt              # YOLOv8 World model
├── output_video.avi              # Generated output video
```

---

## Setup Instructions 🛠️

Follow these steps to run the project smoothly:

### 1. Clone the Repository

```bash
git clone https://github.com/aryaan-dev/object-detection-using-yolo-world.git
cd object-detection-using-yolo-world
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

- `ultralytics` → YOLOv8 models
- `opencv-python` → Video processing
- `supervision` → Bounding box & label annotations

### 4. Download YOLOv8 World Model

Download **`yolov8m-world.pt`** and place it in the project root folder.
This model supports **custom class detection** like cars, people, bikes, etc.

---

## Run the Code ▶️

### For Video File Detection

Make sure `cars.mp4` exists in the project folder, then run:

```bash
python detect.py
```

### For Real-Time Camera Detection

In `detect.py`, change:

```python
cap = cv2.VideoCapture("cars.mp4")
```

to:

```python
cap = cv2.VideoCapture(0)
```

---

## Output 📤

- 📹 Live detection window with bounding boxes and labels
- 💾 Saved output video as `output_video.avi`
- Press **`c`** to stop detection manually

---

## Customization 🎯

You can easily change detection classes:

```python
model.set_classes(["car"])
```

Examples:

```python
["person"]
["car", "bus", "truck"]
["bicycle", "motorcycle"]
```

---

## Troubleshooting 🛑

Common issues and fixes:

- **Video not opening**
  - Check if `cars.mp4` exists and path is correct
- **Model file not found**
  - Ensure `yolov8m-world.pt` is in the root directory
- **Low FPS or lag**
  - Try a lighter model like `yolov8n-world.pt`
- **Webcam not working**
  - Change camera index from `0` to `1`
- **Output video not saved**
  - Ensure the program exits properly using the `c` key

---

## Tips for Beginners 🌟

- Start with video files before switching to real-time camera
- Use lighter models for low-end systems
- Experiment with multiple classes

---

## Created With ❤️ By [ ARYAAN-DEV ]

Feel free to *improve*, *fork* or *share* this project.
Happy detecting 🎯

