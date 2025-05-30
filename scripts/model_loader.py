import random

def load_model():
    return "mock_model"

def predict(model, img):
    # Simulated prediction
    label = random.choice(["underfill", "correct", "overfill"])
    confidence = round(random.uniform(0.7, 0.99), 2)
    return label, confidence
