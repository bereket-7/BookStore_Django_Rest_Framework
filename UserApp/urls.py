from django.urls import path
from .api import UserCreateApi

urlpatterns = [
    path('register', UserCreateApi),
]
