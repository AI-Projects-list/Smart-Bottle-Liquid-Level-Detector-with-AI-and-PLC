# 🧪 Smart Bottle Liquid Level Detection with AI & PLC Integration

This project uses computer vision and AI to detect the liquid level inside bottles on a conveyor. Based on AI classification (underfill, correct, overfill), it sends output to a PLC to separate the bottles accordingly. All inspection results are stored in a database for traceability.

---

## 📦 Features

- Real-time image capture from a webcam
- AI model to detect and classify liquid levels
- Serial communication to PLC (e.g., Modbus/RS232)
- SQLite database logging
- Configurable via YAML file

---

## 🛠️ Tech Stack

- Python
- OpenCV
- SQLite
- PySerial
- (Optional) YOLOv5 / YOLOv8 for real model

---

## 📁 Project Structure

```
smart_bottle_ai/
├── data/                 # Training data (underfill, correct, overfill)
├── model/                # Place your AI model here
├── scripts/
│   ├── infer_and_control.py  # Main pipeline
│   ├── db_logger.py          # Logs to SQLite
│   ├── plc_comm.py           # Sends signal to PLC
│   └── model_loader.py       # Mock or real model loader
├── utils/
│   └── camera_utils.py       # Camera capture
├── requirements.txt
├── app_config.yaml
└── README.md
```

---

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the system:**
   ```bash
   python scripts/infer_and_control.py
   ```

3. **Ensure your camera is connected and PLC is listening on `/dev/ttyUSB0`.**

---

## ⚙️ Configuration

Edit `app_config.yaml` to configure:

```yaml
serial_port: /dev/ttyUSB0
baud_rate: 9600
model_path: ./model/best.pt
database: ./inspection_results.db
```

---

## 🧠 AI Model Notes

- The current model in `model_loader.py` is a **mock simulation**.
- Replace with a real model using YOLOv5 or YOLOv8 for production.
- You can label your dataset using [Roboflow](https://roboflow.com/) or similar.
- Train with `train.py` from YOLOv5 repo and export `best.pt` to `model/`.

---

## 🔧 PLC Control

- Serial port used: `/dev/ttyUSB0`
- Baud rate: 9600
- Sent signal: `0 = underfill`, `1 = correct`, `2 = overfill`

---

## 💾 Database Schema

SQLite database `inspection_results.db` stores:

| Column          | Type     |
|------------------|----------|
| id               | INTEGER  |
| timestamp        | TEXT     |
| image_path       | TEXT     |
| prediction_label | TEXT     |
| prediction_score | REAL     |
| plc_output       | INTEGER  |

---

## 🖼️ Example Image Capture

Captured images saved as `captured_image.jpg` on each inference.

---

## 📈 Future Improvements

- Real-time web dashboard using Flask
- Live camera feed monitoring
- Model retraining and improvement loop
- Upload to cloud (e.g., Firebase, GCP, AWS)

