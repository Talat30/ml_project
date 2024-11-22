# ml_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
import joblib
import numpy as np
import os

# Load the trained model
model_path = os.path.join(os.getcwd(), 'ml_app', 'iris_model.pkl')
model = joblib.load(model_path)

def predict(request):
    # Render the prediction page
    return render(request, 'ml_app/predict.html')

def make_prediction(request):
    if request.method == "POST":
        # Get the input data from the form
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Prepare the data for prediction
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Make the prediction
        prediction = model.predict(input_data)
        predicted_class = prediction[0]

        # Map the predicted class to the Iris species
        species_map = {0: 'Iris Setosa', 1: 'Iris Versicolour', 2: 'Iris Virginica'}
        predicted_species = species_map.get(predicted_class, "Unknown")

        # Return the result on the same page
        return render(request, 'ml_app/predict.html', {'predicted_species': predicted_species})

