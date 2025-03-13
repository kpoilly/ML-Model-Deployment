# Example of Machine Learning Model Deployment with Flask and Docker

This repository contains a simple example of deploying a Machine Learning model via a Flask REST API, containerized with Docker.

The model used for this example is trained for binary classification of breast cancer diagnosis.

## Prerequisites

*   Docker installed on your machine.

## Instructions

**1.	You can simply build and run the Docker container with:**

    ```bash
    make
    ```


   **To Down the docker container:**
   
    ```bash
    make down 
    ```


   **To Up it again:**
   
    ```bash
    make up
    ```


**2.	Test the API:**

   You can use `curl` or a tool like Postman to send a POST request to the API. For example:


    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{'features'}' http://localhost:5000/predict
    ```


   The JSON response will contain the model's prediction (with a probability for each class).


   for example:
   
	```bash
	curl -X POST -H "Content-Type: application/json" -d '{
    "radius_mean": 11.85, "texture_mean": 17.46, "perimeter_mean": 75.54, "area_mean": 432.7, "smoothness_mean": 0.08372, "compactness_mean": 0.05642, "concavity_mean": 0.02688, "concave_points_mean": 0.0228, "symmetry_mean": 0.1875, "fractal_dimension_mean": 0.05715,
    "radius_SE": 0.207, "texture_SE": 1.238, "perimeter_SE": 1.234, "area_SE": 13.88, "smoothness_SE": 0.007595, "compactness_SE": 0.015, "concavity_SE": 0.01412, "concave_points_SE": 0.008578, "symmetry_SE": 0.01792, "fractal_dimension_SE": 0.001784,
    "radius_worst": 13.06, "texture_worst": 25.75, "perimeter_worst": 84.35, "area_worst": 517.8, "smoothness_worst": 0.1369, "compactness_worst": 0.1758, "concavity_worst": 0.1316, "concave_points_worst": 0.0914, "symmetry_worst": 0.3101, "fractal_dimension_worst": 0.07007
	}' http://localhost:5000/predict
	```
 
   Should give you a high probability of being benign.
   
   While
   
		```bash
	curl -X POST -H "Content-Type: application/json" -d '{
    "radius_mean": 20.16, "texture_mean": 19.66, "perimeter_mean": 131.1, "area_mean": 1274, "smoothness_mean": 0.0802, "compactness_mean": 0.08564, "concavity_mean": 0.1155, "concave_points_mean": 0.07726, "symmetry_mean": 0.1928, "fractal_dimension_mean": 0.05096,
    "radius_SE": 0.5925, "texture_SE": 0.6863, "perimeter_SE": 3.868, "area_SE": 74.85, "smoothness_SE": 0.004536, "compactness_SE": 0.01376, "concavity_SE": 0.02645, "concave_points_SE": 0.01247, "symmetry_SE": 0.02193, "fractal_dimension_SE": 0.001589,
    "radius_worst": 23.06, "texture_worst": 23.03, "perimeter_worst": 150.2, "area_worst": 1657, "smoothness_worst": 0.1054, "compactness_worst": 0.1537, "concavity_worst": 0.2606, "concave_points_worst": 0.1425, "symmetry_worst": 0.3055, "fractal_dimension_worst": 0.05933
	}' http://localhost:5000/predict
	```
 
   Should give you the opposite.

## Files

*   `app.py`: Flask API application code.
*   `model/model.pth`: Pre-trained pytorch model.
*   `model/scaler.pkl`: Fitted standard scaler .
*   `Dockerfile`: Dockerfile to build the Docker image.
*   `requirements.txt`: List of Python dependencies.
*   `README.md`: This file.

## Notes

*	The model used in this example is one of the previous model I worked on, you can find it own repo [here](https://github.com/kpoilly/Multilayer-Perceptron).
*	I trained it and optimized it to achieve 99% of accuracy with the dataset that can be found in its repo.
*   This example is simplified to illustrate the concept of deployment. In a real-world context, more robustness should be added (error handling, data validation, security, monitoring, etc.).
