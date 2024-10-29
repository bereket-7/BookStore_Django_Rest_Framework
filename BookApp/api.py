from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from BookApp.models import BookModel
from .serializers import BookSerializer


@api_view(['GET'])
def BookListApi(request):
    books = BookModel.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def BookCreateApi(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Book created successfully', 'book': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def BookUpdateApi(request, id):
    try:
        book = BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Book updated successfully', 'book': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def BookDeleteApi(request, id):
    try:
        book = BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# End of File
