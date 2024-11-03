# views.py
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import NegociosUsers, AuthtokenToken

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    object_negocio_user = NegociosUsers.objects.get(id_user=user.id)
    id_negocio = object_negocio_user.id_negocio
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        object_key = AuthtokenToken.objects.get(key = token.key)
        object_key.id_negocio = id_negocio
        object_key.save()
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout(request):
    try:
        request.user.auth_token.delete()  # Elimina el token del usuario
        return Response(status=status.HTTP_200_OK)
    except (AttributeError, Exception):
        return Response(status=status.HTTP_400_BAD_REQUEST)
