from rest_framework import serializers
from service.models import Funcionamiento
from service.models import Estacion

class FuncionamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionamiento
        fields = ('fecha', 'valor')

class EstacionSerializer(serializers.ModelSerializer):
    funcionamiento = FuncionamientoSerializer(many=True, read_only=True)

    class Meta:
        model = Estacion
        fields = ('estacion','latitud','longitud', 'administrador','funcionamiento')
        