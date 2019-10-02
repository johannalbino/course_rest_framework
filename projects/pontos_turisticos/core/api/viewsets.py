from rest_framework import viewsets
from core.models import PontoTuristicos
from .serializers import PontoTuristicosSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing.
    """
    queryset = PontoTuristicos.objects.all()
    serializer_class = PontoTuristicosSerializer
