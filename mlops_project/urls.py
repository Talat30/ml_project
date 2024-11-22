# mlops_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ml_app.urls')),  # This will map the root URL to ml_app
]
