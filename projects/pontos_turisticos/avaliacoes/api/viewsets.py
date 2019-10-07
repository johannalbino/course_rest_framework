from rest_framework import viewsets
from core.models import Avaliacoes
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
