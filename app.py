import torch
import pickle
import numpy as np
from flask import Flask, request, jsonify

from models import Network

app = Flask(__name__)

model = Network(30, 2, 16, 2)
model.load_state_dict(torch.load("model/model.pth", map_location=torch.device('cpu')))
with open('model/scaler.pkl','rb') as f:
    model.scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feature_names = [
                         'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
                         'radius_SE', 'texture_SE', 'perimeter_SE', 'area_SE', 'smoothness_SE', 'compactness_SE', 'concavity_SE', 'concave_points_SE', 'symmetry_SE', 'fractal_dimension_SE',
                         'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst',
                         ]
        features_list = [data[feature_name] for feature_name in feature_names]
        features = np.array(features_list).reshape(1, -1)
        prediction = model.predict(features).tolist()[0]
        prediction_dict = {
            "Benign": round(prediction[0], 5),
            "Malignant": round(prediction[1], 5)
        }
        return jsonify({'prediction': prediction_dict})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)