from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np
import tensorflow as tf
from io import BytesIO

app = FastAPI()
model = tf.keras.models.load_model("cats_vs_dogs_mobilenetv2.keras")

def preprocess_image(image_bytes):
    img = Image.open(BytesIO(image_bytes)).convert("RGB").resize((160, 160))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    return img_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img_array = preprocess_image(img_bytes)
    pred = model.predict(img_array)[0][0]
    label = "Dog" if pred > 0.5 else "Cat"
    return {"label": label, "confidence": float(pred)}
