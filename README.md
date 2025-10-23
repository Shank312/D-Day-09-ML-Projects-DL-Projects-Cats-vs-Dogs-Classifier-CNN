

# 🐶🐱 Cats vs Dogs Classifier (MobileNetV2)

<p align="center">
  <img src="https://img.shields.io/badge/Framework-TensorFlow-orange?logo=tensorflow" alt="TensorFlow">
  <img src="https://img.shields.io/badge/Model-MobileNetV2-blue?logo=keras" alt="Model">
  <img src="https://img.shields.io/badge/Language-Python-green?logo=python" alt="Language">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success" alt="Status">
</p>

A deep learning project that classifies images as **Cat** or **Dog** using **MobileNetV2** trained with **TensorFlow/Keras**.

---

## 🚀 Project Overview
This project implements a **Convolutional Neural Network (CNN)** built on **MobileNetV2** to classify cats and dogs.  
The model is optimized for lightweight deployment — ideal for mobile or web inference.

---

## 🧩 Features
✅ Transfer learning using MobileNetV2  
✅ TensorFlow / Keras-based model  
✅ Ready for deployment with `.keras` or `.tflite` format  
✅ Supports Google Colab & local execution  
✅ Inference-ready `app.py` script  

---

## 📁 Folder Structure

Cats vs Dogs Classifier (CNN)/
│
├── app.py # Inference script
├── requirements.txt # Dependencies
├── README.md # Documentation
├── LICENSE # License file (MIT)
├── .gitignore # Ignored files (outputs, logs, env)
└── cats_vs_dogs_mobilenetv2.keras #



---

## ⚙️ Setup Instructions

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/Shank312/D-Day-09-ML-Projects-DL-Projects-Cats-vs-Dogs-Classifier-CNN.git
cd D-Day-09-ML-Projects-DL-Projects-Cats-vs-Dogs-Classifier-CNN


2️⃣ Install Dependencies:
pip install -r requirements.txt


3️⃣ Download Model

If you haven't included the .keras file in the repo:

Download it manually from Google Drive:
/MyDrive/cats-vs-dogs/outputs/cats_vs_dogs_mobilenetv2.keras

Or create a download_model.sh script using:
#!/bin/bash
mkdir -p outputs
# pip install gdown
# gdown --id <YOUR_DRIVE_FILE_ID> -O outputs/cats_vs_dogs_mobilenetv2.keras


4️⃣ Run the App
python app.py


🧠 Model Architecture

Base Model: MobileNetV2 (pretrained on ImageNet)

Input Shape: 160×160×3

Optimizer: Adam

Loss: Binary Crossentropy

Metrics: Accuracy

Training Augmentations:

Random Flip

Random Rotation

Random Zoom


📊 Results:
|        Metric        |  Value |
| :------------------: | :----: |
|   Training Accuracy  |  ~98%  |
|  Validation Accuracy |  ~96%  |
|  Model Size (.keras) |  24 MB |
| Model Size (.tflite) | 2.4 MB |

✅ Lightweight and deployable on edge/mobile devices.


🧪 Example Inference
python app.py --image path_to_image.jpg

Expected Output:
Prediction: Dog 🐶 (Confidence: 97.8%)


📦 Dependencies

TensorFlow

NumPy

Pillow

Flask (if running web app)

gdown (for downloading model)

Install via:
pip install -r requirements.txt


🖼️ Dataset

Dataset used: Kaggle Dogs vs Cats
Link: https://www.kaggle.com/c/dogs-vs-cats

The dataset contains 25,000 labeled images (12.5k cats, 12.5k dogs).


🌍 Deployment Options

You can deploy this model as:

🧠 Flask / FastAPI app

☁️ TensorFlow Serving REST API

📱 TensorFlow Lite for Android/iOS

🕸️ Streamlit Web App


🔥 Future Enhancements

 Streamlit UI for web demo

 Real-time webcam inference

 Convert to ONNX for cross-framework compatibility

 Add Grad-CAM visualization for explainability


📜 License

This project is licensed under the MIT License.


👨‍💻 Author

Shankar Kumar
📧 shankar312@gmail.com
🌐 https://github.com/Shank312


⭐ Acknowledgements

TensorFlow & Keras Teams

Kaggle Dataset Contributors

Google Colab for Training Environment


⭐ If you like this project, give it a star on GitHub! ⭐
