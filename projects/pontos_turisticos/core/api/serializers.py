from rest_framework import serializers
from core.models import PontoTuristicos

class PontoTuristicosSerializer(serializers.ModelSerializer):

    class Meta:
        model = PontoTuristicos
        fields = ('__all__')