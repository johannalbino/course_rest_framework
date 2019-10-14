from rest_framework import viewsets
from core.models import Atracoes
from .serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):

    queryset = Atracoes.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ['id', 'name', 'description']