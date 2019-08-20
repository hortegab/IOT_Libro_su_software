
from rest_framework import serializers
from .models import Temperatura, PH, O2disuelto, Pozo #llama los modelos creados para nuestra API

class TemperaturaSerializer(serializers.ModelSerializer):
    """Serializa el modelo temperatura """
    class Meta:
        model = Temperatura
        fields = "__all__"

class PHSerializer(serializers.ModelSerializer):
    """Serializa el modelo PH """
    class Meta:
        model = PH
        fields = "__all__"

class O2disueltoSerializer(serializers.ModelSerializer):
    """Serializa el modelo O2disuelto """
    class Meta:
        model = O2disuelto
        fields = "__all__"

class PozoSerializer(serializers.ModelSerializer):
    """Serializa el modelo Pozo """
    class Meta:
        model = Pozo
        fields = "__all__"