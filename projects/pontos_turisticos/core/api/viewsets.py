from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from core.models import PontoTuristicos
from .serializers import PontoTuristicosSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing.
    """
    queryset = PontoTuristicos.objects.all()
    serializer_class = PontoTuristicosSerializer
    filter_backends = [SearchFilter]
    filter_fields = ['id', 'name', 'description', 'endereco__linha1']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = PontoTuristicos.objects.all()

        if id:
            queryset = PontoTuristicos.objects.filter(pk=id)

        elif name:
            queryset = queryset.objects.filter(name=name)

        elif description:
            queryset = queryset.objects.filter(description=description)

        return queryset

    """
    def list(self, request, *args, **kwargs):
        
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
    
        queryset = PontoTuristicos.objects.all()
        serializer = PontoTuristicosSerializer(queryset, many=True)
        return Response(serializer.data)
        
    """

    def create(self, request, *args, **kwargs):
        """
        Função para criar um novo objeto no banco de dados ou na aplicação em geral.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        """
        Para remover
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def retrieve(self, request, *args, **kwargs):
        """
        Para acessar recurso de um objeto
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def update(self, request, *args, **kwargs):
        """
        Para atualizar o objeto
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def partial_update(self, request, *args, **kwargs):
        """
        Para atualizar somente alguns campos do objeto (PATCH)
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        """
        Metodo propria para alterar
        :param request:
        :param pk:
        :return:
        """
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        """
        Action proprio
        :param request:
        :return:
        """
        pass