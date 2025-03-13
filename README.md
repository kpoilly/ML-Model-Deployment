# ML-Model-Deployment
This project is about deploying a model using Docker and Flask.


curl -X POST -H "Content-Type: application/json" -d '{
    "radius_mean": 17.99, "texture_mean": 10.38, "perimeter_mean": 122.8, "area_mean": 1001.0, "smoothness_mean": 0.1184, "compactness_mean": 0.2776, "concavity_mean": 0.3001, "concave_points_mean": 0.1471, "symmetry_mean": 0.2419, "fractal_dimension_mean": 0.07871,
    "radius_SE": 1.095, "texture_SE": 0.9053, "perimeter_SE": 8.589, "area_SE": 153.4, "smoothness_SE": 0.006399, "compactness_SE": 0.04904, "concavity_SE": 0.05373, "concave_points_SE": 0.01587, "symmetry_SE": 0.03003, "fractal_dimension_SE": 0.006193,
    "radius_worst": 25.41, "texture_worst": 17.33, "perimeter_worst": 184.6, "area_worst": 2019.0, "smoothness_worst": 0.1622, "compactness_worst": 0.6656, "concavity_worst": 0.7119, "concave_points_worst": 0.2654, "symmetry_worst": 0.4601, "fractal_dimension_worst": 0.1189
}' http://localhost:5000/predict

-> Malignant

curl -X POST -H "Content-Type: application/json" -d '{
    "radius_mean": 11.85, "texture_mean": 17.46, "perimeter_mean": 75.54, "area_mean": 432.7, "smoothness_mean": 0.08372, "compactness_mean": 0.05642, "concavity_mean": 0.02688, "concave_points_mean": 0.0228, "symmetry_mean": 0.1875, "fractal_dimension_mean": 0.05715,
    "radius_SE": 0.207, "texture_SE": 1.238, "perimeter_SE": 1.234, "area_SE": 13.88, "smoothness_SE": 0.007595, "compactness_SE": 0.015, "concavity_SE": 0.01412, "concave_points_SE": 0.008578, "symmetry_SE": 0.01792, "fractal_dimension_SE": 0.001784,
    "radius_worst": 13.06, "texture_worst": 25.75, "perimeter_worst": 84.35, "area_worst": 517.8, "smoothness_worst": 0.1369, "compactness_worst": 0.1758, "concavity_worst": 0.1316, "concave_points_worst": 0.0914, "symmetry_worst": 0.3101, "fractal_dimension_worst": 0.07007
}' http://localhost:5000/predict

-> Benign