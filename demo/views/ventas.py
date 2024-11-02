from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Venta, DetalleVentas
from ..serializers.ventas import Ventas_Serializer, Comprobantes_Serializer, Comprobante_Serializer


#api/ventas/
@api_view(['GET'])
def listar_ventas(request):
    # Obtener todos los registros de Venta
    
    ventas = list(DetalleVentas.objects.filter(id_negocio=1).values())
    # Devolver los datos serializados como JSON
    return JsonResponse(ventas, safe=False)

#api/venta/nuevo
@api_view(['POST'])
def nueva_venta(request):
    serializer = Comprobante_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)  # Imprimir errores de validación para depuración
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api/ventas/comprobantes/
@api_view(['GET'])
def comprobantes(request):
    # Obtener todos los registros de Venta
    ventas = Venta.objects.filter(id_negocio=1)
    # Serializar los datos
    serializer = Comprobantes_Serializer(ventas, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)

#api/ventas/comprobante/<str:serie>-<int:numero>
@api_view(['GET'])
def comprobante(request, serie, numero):
    # Obtener todos los registros de Venta
    ventas = Venta.objects.filter(id_negocio=1, id_serie__serie=serie, numero_serie = numero)
    # Serializar los datos
    serializer = Comprobante_Serializer(ventas, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)

