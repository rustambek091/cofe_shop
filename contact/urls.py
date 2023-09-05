from django.urls import path
from .views import register

urlpatterns = [
    # Boshqa URL manzillar
    path('register/', register, name='register'),
]