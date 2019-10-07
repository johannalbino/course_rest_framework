from rest_framework import viewsets
from rest_framework.response import Response

from core.models import PontoTuristicos
from .serializers import PontoTuristicosSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing.
    """
    serializer_class = PontoTuristicosSerializer

    def get_queryset(self):
        return PontoTuristicos.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = PontoTuristicos.objects.filter(id=2)
        serializer = PontoTuristicosSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Função para criar um novo objeto no banco de dados ou na aplicação em geral.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

    def destroy(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """