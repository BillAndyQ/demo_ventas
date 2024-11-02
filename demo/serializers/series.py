from rest_framework import serializers
from ..models import Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id_serie','serie','tipo_serie']