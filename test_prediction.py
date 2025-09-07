import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import json

# Paths
MODEL_PATH = os.path.join("artifacts", "training", "model.keras")
CLASS_MAP_PATH = os.path.join("artifacts", "training", "class_indices.json")

# Load class mapping safely
def load_class_mapping():
    if os.path.exists(CLASS_MAP_PATH):
        with open(CLASS_MAP_PATH, "r") as f:
            class_indices = json.load(f)
        # Flip keys/values so 0 → "Coccidiosis", etc.
        return {v: k for k, v in class_indices.items()}
    else:
        print("[INFO] class_indices.json not found. Using default mapping...")
        return {0: "Coccidiosis", 1: "Healthy"}

# Prediction function
def predict_image(img_path):
    # Load model
    model = load_model(MODEL_PATH)

    # Preprocess image
    test_image = image.load_img(img_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    # Prediction
    preds = model.predict(test_image)
    result = np.argmax(preds, axis=1)[0]

    # Map index to class
    idx_to_class = load_class_mapping()
    prediction = idx_to_class.get(result, "Unknown")

    print(f"Predicted Class: {prediction}")
    return prediction


if __name__ == "__main__":
    TEST_IMAGE = r"datasets\Chicken-fecal-images\Coccidiosis\cocci.0.jpg"  # change path if needed
    predict_image(TEST_IMAGE)
