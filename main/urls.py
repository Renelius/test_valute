from django.urls import path
from .views import index, get_value

urlpatterns = [
    path('index', index),
    path('get_value', get_value)
]