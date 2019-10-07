from rest_framework import viewsets
from core.models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer