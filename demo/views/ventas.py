from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Venta
from ..serializers.ventas import Ventas_Serializer, Comprobantes_Serializer, Comprobante_Serializer

@api_view(['GET'])
def listar_ventas(request):
    # Obtener todos los registros de Venta
    ventas = Venta.objects.filter(id_negocio=1)
    # Serializar los datos
    serializer = Ventas_Serializer(ventas, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)

@api_view(['GET'])
def comprobantes(request):
    # Obtener todos los registros de Venta
    ventas = Venta.objects.filter(id_negocio=1)
    # Serializar los datos
    serializer = Comprobantes_Serializer(ventas, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)

@api_view(['GET'])
def comprobante(request, serie, numero):
    # Obtener todos los registros de Venta
    ventas = Venta.objects.filter(id_negocio=1, id_serie__serie=serie, numero_serie = numero)
    # Serializar los datos
    serializer = Comprobante_Serializer(ventas, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)

# @permission_classes
class Ventas(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

    def get(self, request):
        # Aquí puedes agregar la lógica que desees
        return Response({"message": "Hola, estás autenticado!"}, status=status.HTTP_200_OK)