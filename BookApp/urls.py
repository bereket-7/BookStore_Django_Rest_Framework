from django.urls import path
from .api import BookListApi

urlpatterns = [
    path('list', BookListApi)
]
