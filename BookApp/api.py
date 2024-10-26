from rest_framework.decorators import api_view
from rest_framework.response import Response

from BookApp.models import BookModel


@api_view(['GET'])
def BookListApi(request):
    books = BookModel.objects.all()

    books = [{
        'name': book.name,
        'author': book.author} for book in books]
    return Response(books)
