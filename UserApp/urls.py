from django.urls import path
from .api import BookCreateApi, BookListApi, BookUpdateApi, BookDeleteApi

urlpatterns = [
    path('list', BookListApi),
]
