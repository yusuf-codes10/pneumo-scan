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
model = load_model('models/cnn_xray_v1.h5')  # or .h5

# Example classes
classes = ['NORMAL', 'PNEUMONIA']

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    # Open image
    img = Image.open(file).convert('RGB')

    # Resize to the same size your model was trained on
    img = img.resize((224, 224))

    # Convert to numpy array and normalize
    img_array = np.array(img) / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    pred = model.predict(img_array)

    # Get class index
    class_idx = np.argmax(pred, axis=1)[0]

    # Get confidence
    confidence = float(np.max(pred))

    return jsonify({
        'prediction': classes[class_idx],
        'confidence': confidence
    })




@app.route('/predict', methods=['GET'])
def send_prediction():
    return '{Your request has been sent}'

if __name__ in "__main__":
    app.run(debug=True)