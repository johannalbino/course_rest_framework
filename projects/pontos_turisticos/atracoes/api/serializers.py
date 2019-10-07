from rest_framework import serializers
from core.models import Atracoes

class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracoes
        fields = ('__all__')