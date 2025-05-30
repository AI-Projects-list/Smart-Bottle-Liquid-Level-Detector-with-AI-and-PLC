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

