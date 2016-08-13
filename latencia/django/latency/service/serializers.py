from rest_framework import serializers
from service.models import Estado
from service.models import Estacion

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('fecha','valor')

class EstacionSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(many=True, read_only=True)
    class Meta:
        model = Estacion
        fields = ('estacion','latitud','longitud', 'administrador','estado')