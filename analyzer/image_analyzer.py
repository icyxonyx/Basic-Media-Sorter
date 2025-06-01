from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import EfficientNetB3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as keras_image
from utils.label_mapper import map_labels_to_category

model = EfficientNetB3(weights='imagenet')

def classify_image(img):
    img = img.resize((300, 300))
    x = keras_image.img_to_array(img)
    x = preprocess_input(np.expand_dims(x, axis=0))
    preds = model.predict(x)
    labels = decode_predictions(preds, top=5)[0]
    filtered = [label.lower() for (_, label, prob) in labels if prob > 0.6]
    print(f"[DEBUG] Predictions: {labels} | Filtered: {filtered}")
    return filtered

def analyze_image_file(img_path):
    try:
        img = Image.open(img_path)
        labels = classify_image(img)
        return [map_labels_to_category(labels)]
    except Exception as e:
        print(f"Error in analyze_image_file({img_path}): {e}")
        return ["Uncategorized"]
