from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Venta, DetalleVentas, Serie, AuthtokenToken
from ..serializers.ventas import Ventas_Serializer, Comprobantes_Serializer, Comprobante_Serializer
from datetime import datetime

#api/ventas/
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_ventas(request):
    # Obtener el id relacionado al negocio
    token = request.user.auth_token.key
    object_token = AuthtokenToken.objects.get(key=token)
    id_negocio = object_token.id_negocio
    
    ventas = list(DetalleVentas.objects.filter(id_negocio=id_negocio).values())
    # Devolver los datos serializados como JSON
    return JsonResponse(ventas, safe=False)

#api/venta/nueva
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def nueva_venta(request):
    # Extraer detalles de productos del JSON
    token = request.user.auth_token.key
    try:
        object_token = AuthtokenToken.objects.get(key=token)
    except AuthtokenToken.DoesNotExist:
        return Response({'error': 'Token no válido.'}, status=status.HTTP_401_UNAUTHORIZED)
    id_negocio = object_token.id_negocio
    
    detalles = request.data.get("detalles", [])
    serie = request.data.get("serie")
    
    try:
        object_serie = Serie.objects.get(serie=serie, id_negocio=id_negocio)
    except Serie.DoesNotExist:
        return Response({'error': 'La serie especificada no existe.'}, status=status.HTTP_404_NOT_FOUND)

    last_num_serie = object_serie.ultimo_num
    
    if(last_num_serie == None):
        request.data['numero_serie'] = 1
    else:
        request.data['numero_serie'] = last_num_serie + 1
        
    # Calcular el total de la venta sumando los subtotales de cada detalle
    total_venta = sum(detalle.get("precio_subtotal", 0) for detalle in detalles)
    
    # Añadir el total de venta calculado al JSON de entrada
    request.data["total_venta"] = total_venta
    request.data['tipo_comprobante'] = object_serie.tipo_serie
    request.data['fecha_hora'] = datetime.now()
    request.data['id_negocio'] = 1
    
    serializer = Comprobante_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        if(last_num_serie == None):
            object_serie.ultimo_num = 1
        else:
            object_serie.ultimo_num = last_num_serie + 1
        object_serie.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)  # Imprimir errores de validación para depuración
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api/ventas/comprobantes/
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comprobantes(request):
    
    token = request.user.auth_token.key
    object_token = AuthtokenToken.objects.get(key=token)
    id_negocio = object_token.id_negocio
    
    # Obtener todos los registros de Venta
    ventas = Venta.objects.filter(id_negocio=id_negocio)
    # Serializar los datos
    serializer = Comprobantes_Serializer(ventas, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)

#api/ventas/comprobante/<str:serie>-<int:numero>
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comprobante(request, serie, numero):
    token = request.user.auth_token.key
    object_token = AuthtokenToken.objects.get(key=token)
    id_negocio = object_token.id_negocio
    
    # Obtener todos los registros de Venta
    ventas = Venta.objects.filter(id_negocio=id_negocio, id_serie__serie=serie, numero_serie = numero)
    # Serializar los datos
    serializer = Comprobante_Serializer(ventas, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)

