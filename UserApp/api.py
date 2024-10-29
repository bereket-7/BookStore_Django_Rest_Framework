from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def UserCreateApi(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create_user(username=username, password=password)
    user.save()

    return Response({'message': 'User created successfully', 'user': {'username': user.username}}, status=status.HTTP_201_CREATED)
