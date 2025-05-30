import sqlite3
from datetime import datetime

def log_result(image_path, label, confidence, plc_output):
    conn = sqlite3.connect('inspection_results.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bottle_inspection (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            image_path TEXT,
            prediction_label TEXT,
            prediction_score REAL,
            plc_output INTEGER
        )
    """)

    cursor.execute("""
        INSERT INTO bottle_inspection (timestamp, image_path, prediction_label, prediction_score, plc_output)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.now().isoformat(), image_path, label, confidence, plc_output))

    conn.commit()
    conn.close()
