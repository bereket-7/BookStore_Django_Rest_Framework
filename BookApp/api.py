from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def BookListApi(request):
    books = [
        {
            'name': 'The Alchemist',
            'author': 'Paulo Coelho',
        },
        {
            'name': '1984',
            'author': 'George Orwell',
        },
        {
            'name': 'To Kill a Mockingbird',
            'author': 'Harper Lee',
        },
        {
            'name': 'Moby Dick',
            'author': 'Herman Melville',
        }

    ]
    return Response(books)
