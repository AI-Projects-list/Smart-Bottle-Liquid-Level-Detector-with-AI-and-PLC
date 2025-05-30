import serial
import time

def send_to_plc(signal):
    try:
        with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
            ser.write(bytes([signal]))
            time.sleep(0.1)
    except Exception as e:
        print(f"Error sending to PLC: {e}")
