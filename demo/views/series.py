from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Serie
from ..serializers.series import SerieSerializer


@api_view(['GET'])
def series(request):
    # Obtener todos los registros de Venta
    series = Serie.objects.filter(id_negocio=1)
    # Serializar los datos
    serializer = SerieSerializer(series, many=True)
    # Devolver los datos serializados como JSON
    return Response(serializer.data)