from django.urls import path
from .api import BookCreateApi, BookListApi, BookUpdateApi, BookDeleteApi

urlpatterns = [
    path('list', BookListApi),
    path('create', BookCreateApi),
    path('<int:id>/update', BookUpdateApi),
    path('<int:id>/delete', BookDeleteApi)
]
