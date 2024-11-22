# ml_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),  # Map the root URL to the 'predict' view
    path('predict/', views.predict, name='predict'),  # Another way to call the prediction page
    path('make_prediction/', views.make_prediction, name='make_prediction'),  # Prediction action
]
