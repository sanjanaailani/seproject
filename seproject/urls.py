from django.contrib import admin  # Add this line
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Ensure this line is correct
]
