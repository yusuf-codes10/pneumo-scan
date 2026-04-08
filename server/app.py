from flask import Flask, request, jsonify
from flask_cors import CORS          # ← add this
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load your model once
model = load_model('model/cnn_xray_v1.keras')  # or .h5

@app.route('/predict', methods=['GET'])
def send_prediction():
    return '{Your request has been sent}'

if __name__ in "__main__":
    app.run(debug=True)