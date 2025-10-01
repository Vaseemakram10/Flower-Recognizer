🌸 Flower Recognizer – Flask Web App

A simple yet powerful flower classification web application built with Flask and TensorFlow.
Users can upload an image or capture one using their webcam, and the model will predict the type of flower in real time.

📂 Project Structure
converted_keras/
├── app.py               # Main Flask application
├── keras_model.h5       # Trained TensorFlow Keras model
├── labels.txt           # Class labels (one per line)
├── static/
│   └── style.css        # Basic styling for the web page
├── templates/
│   └── index.html       # Main HTML interface
└── requirements.txt     # Python dependencies

✨ Features

📷 Upload or capture flower images directly from your device or webcam

👀 Image preview before prediction

⚡ Real-time prediction using a pre-trained deep learning model

🚀 Lightweight Flask backend for fast inference

🛠 Requirements

Python 3.7+

pip (Python package installer)

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/flower-recognizer.git
cd flower-recognizer


Create a virtual environment (recommended)

python -m venv venv
# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


If you don’t have a requirements.txt, create one with:

Flask
tensorflow
numpy
Pillow
opencv-python

▶️ Running the App
python app.py


The app will start locally at:

👉 http://127.0.0.1:5000

📊 Example Prediction

Upload or capture a flower image

Click Predict

The app will display:

🌼 Predicted flower class

📈 Confidence score (%)

📌 Future Improvements

Add support for more flower categories

Deploy the app on Heroku / Render / AWS

Build a mobile-friendly UI

Enable batch image predictions

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.