from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def UserCreateApi(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create_user(username=username, password=password)
    user.save()

    return Response({'message': 'User created successfully', 'user': {'username': user.username}}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def UserLoginApi(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'Login successful', 'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ProtectedApi(request):
    data = {
        'message': 'This is a protected view accessible only with a valid token.',
        'books': [
            {'name': 'Book 1', 'author': 'Author A'},
            {'name': 'Book 2', 'author': 'Author B'}
        ]
    }
    return Response(data)
