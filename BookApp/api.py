from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from BookApp.models import BookModel


@api_view(['GET'])
def BookListApi(request):
    books = BookModel.objects.all()

    books = [{
        'id': book.id,
        'name': book.name,
        'author': book.author} for book in books]
    return Response(books)


@api_view(['POST'])
def BookCreateApi(request):
    name = request.data.get('name')
    author = request.data.get('author')

    if not name or not author:
        return Response({'error': 'Both name and author are required.'}, status=status.HTTP_400_BAD_REQUEST)

    book = BookModel(name=name, author=author)
    book.save()

    return Response({'message': 'Book created successfully', 'book': {'name': book.name, 'author': book.author}}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def BookUpdateApi(request, id):
    try:

        book = BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    name = request.data.get('name')
    author = request.data.get('author')

    if name:
        book.name = name
    if author:
        book.author = author

    book.save()

    return Response({
        'message': 'Book updated successfully',
        'book': {
            'name': book.name,
            'author': book.author
        }
    }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def BookDeleteApi(request, id):
    try:
        book = BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# End of File
