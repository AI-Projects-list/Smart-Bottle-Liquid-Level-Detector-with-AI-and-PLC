from utils.camera_utils import capture_image
from scripts.model_loader import load_model, predict
from scripts.plc_comm import send_to_plc
from scripts.db_logger import log_result

def main():
    model = load_model()
    img = capture_image()

    label, confidence = predict(model, img)

    if label == "underfill":
        plc_signal = 0
    elif label == "correct":
        plc_signal = 1
    else:
        plc_signal = 2

    send_to_plc(plc_signal)
    log_result("captured_image.jpg", label, confidence, plc_signal)

if __name__ == "__main__":
    main()
