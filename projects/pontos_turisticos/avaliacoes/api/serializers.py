from rest_framework import serializers
from core.models import Avaliacoes


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ('__all__')