from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import PontoTuristicos
from .serializers import PontoTuristicosSerializer
from core.models import TypeTest


class PontoTuristicosFilter(filters.FilterSet):
    id = filters.CharFilter(lookup_expr='exact')
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    type1 = filters.ModelChoiceFilter(queryset=TypeTest.objects.all())
    endereco = filters.CharFilter(lookup_expr='icontains', field_name='endereco__linha1')

    class Meta:
        model = PontoTuristicos
        fields = ('id', 'name', 'description', 'type1', 'endereco')


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing.
    """

    serializer_class = PontoTuristicosSerializer
    filterset_class = PontoTuristicosFilter
    #permission_classes = [IsAuthenticated]
    #authentication_classes = [TokenAuthentication, ]

    #lookup_field = 'name'  Tomar cuidado ao utilizar esse metodo

    def get_queryset(self):
        queryset = PontoTuristicos.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        #queryset = PontoTuristicos.objects.all()
        #serializer = PontoTuristicosSerializer(queryset, many=True)
        #return Response(serializer.data)
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

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
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Para acessar recurso de um objeto
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Para atualizar o objeto
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Para atualizar somente alguns campos do objeto (PATCH)
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

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