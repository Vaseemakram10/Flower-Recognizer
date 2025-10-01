from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import base64
import io
from PIL import Image

app = Flask(__name__)

# Load model and labels
model = tf.keras.models.load_model("keras_model.h5")
with open("labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]
IMG_SIZE = (224, 224)

def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array.astype(np.float32)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if "image" not in data:
        return jsonify({"error": "No image data"}), 400

    image_data = data["image"].split(",")[1]
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    top_index = np.argmax(predictions[0])
    top_class = class_names[top_index]
    confidence = float(predictions[0][top_index])

    return jsonify({
        "class": top_class,
        "confidence": f"{confidence:.2%}"
    })

if __name__ == "__main__":
    app.run(debug=True)
