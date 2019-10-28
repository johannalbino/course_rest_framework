from rest_framework import viewsets
from core.models import TypeTest
from .serializer import TypeTestSerializer


class TypeTestViewSet(viewsets.ModelViewSet):
    queryset = TypeTest.objects.all()
    serializer_class = TypeTestSerializer
