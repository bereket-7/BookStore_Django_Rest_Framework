from django.urls import path
from .api import UserCreateApi, UserLoginApi

urlpatterns = [
    path('register', UserCreateApi),
    path('login', UserLoginApi),
]
