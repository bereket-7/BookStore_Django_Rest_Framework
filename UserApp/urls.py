from django.urls import path
from .api import ProtectedApi, UserCreateApi, UserLoginApi

urlpatterns = [
    path('register', UserCreateApi),
    path('login', UserLoginApi),
    path('protected', ProtectedApi),
]
