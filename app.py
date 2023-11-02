# simple endpoint app
from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)

def load_model():
    return load('model.joblib') 

@app.route('/')
def home():
    return "Breast Cancer Predictions. Use /predict for predictions."

@app.route('/predict', methods=['POST'])
def predict():
     # Get the data from the request
    data = pd.DataFrame.from_dict(request.get_json())

    model = load_model()
    preds = model.predict(data)

    return jsonify({'predictions': list(preds)})

# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
