# serializers.py
from rest_framework import serializers
from ..models import Venta, Serie, DetalleVentas

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['serie']

class Detalle_comprobante_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVentas
        fields = ['id_detalle_venta','id_producto','nombre_producto','precio_unit','cantidadxprod','precio_subtotal']

class Ventas_Serializer(serializers.ModelSerializer):
    serie = serializers.SerializerMethodField()
    class Meta:
        model = Venta
        fields = ['id_venta','fecha_hora','tipo_comprobante','numero_serie','serie']
    
    def get_serie(self, obj):
        # Retorna solo el valor del campo 'serie' de la relación 'id_serie'
        return obj.id_serie.serie if obj.id_serie else None

class Comprobantes_Serializer(serializers.ModelSerializer):
    serie = serializers.SerializerMethodField()
    class Meta:
        model = Venta
        fields = ['id_venta','fecha_hora','tipo_comprobante','numero_serie','serie']
    
    def get_serie(self, obj):
        # Retorna solo el valor del campo 'serie' de la relación 'id_serie'
        return obj.id_serie.serie if obj.id_serie else None
    
class Comprobante_Serializer(serializers.ModelSerializer):
    # serie = serializers.SerializerMethodField()
    serie = serializers.CharField(write_only=True)
    detalles = Detalle_comprobante_Serializer(many=True)
    class Meta:
        model = Venta
        fields = ["id_negocio",'id_venta','fecha_hora','tipo_comprobante', 'metodo_pago','serie', 'numero_serie','nombre_cliente', 'dni_ruc', 'telefono' ,'total_venta','detalles']
        
    def get_serie(self, obj):
        # Retorna solo el valor del campo 'serie' de la relación 'id_serie'
        return obj.id_serie.serie if obj.id_serie else None
    
    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        
        # Extraer y asignar 'serie' a 'id_serie' en el modelo Venta
        serie_value = validated_data.pop('serie', None)
        if serie_value:
            # Buscar o crear el objeto relacionado de la serie
            id_serie_instance, created = Serie.objects.get_or_create(serie=serie_value)
            validated_data['id_serie'] = id_serie_instance

        # Crear la venta con los datos validados y el id_serie
        venta = Venta.objects.create(**validated_data)

        # Crear los detalles de la venta
        for detalle_data in detalles_data:
            DetalleVentas.objects.create(id_venta=venta, **detalle_data)

        return venta