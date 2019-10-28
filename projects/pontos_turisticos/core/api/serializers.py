from rest_framework import serializers
from core.models import PontoTuristicos, Atracoes, Comentarios, Endereco, Avaliacoes, DocIdentificacao, TypeTest
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class DocIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicosSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)
    doc_identificacao = DocIdentificacaoSerializer(many=False)
    type1 = serializers.PrimaryKeyRelatedField(
        queryset=TypeTest.objects.filter(type='Luis'), many=False
    )
    type2 = serializers.PrimaryKeyRelatedField(
        queryset=TypeTest.objects.filter(type='Jose'), many=False
    )


    class Meta:
        model = PontoTuristicos
        fields = ('id', 'name', 'description', 'aprovado', 'photo', 'atracoes', 'type1', 'type2', 'comentarios', 'avaliacoes', 'endereco', 'doc_identificacao')
        read_only_fields = ('comentarios', 'avaliacoes', 'endereco')

    def create_relations_many_to_many(self, ponto, *args, **kwargs):
        models = [Atracoes, Comentarios, Avaliacoes]
        campos_pk = [ponto.atracoes, ponto.comentarios, ponto.avaliacoes]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                at = rel[0].objects.create(**rel[2][0])
                rel[1].add(at)

    def create_relations_one_to_one(self, _field_one_to_one, *args, **kwargs):

        _data_one = []

        for one_to_one in _field_one_to_one:
            _data_one.append(args[0][one_to_one])
            del args[0][one_to_one]

        ponto = PontoTuristicos

        models = [Endereco, DocIdentificacao]
        campos_pk = [ponto.endereco, ponto.doc_identificacao]

        relations = list(zip(models, campos_pk, _data_one,_field_one_to_one))
        ponto = PontoTuristicos.objects.create(**args[0])

        if args.__len__() > 0:
            for rel in relations:
                rel_list = list(rel)
                if rel[2] is None:
                    _relation_data = rel_list[0].objects.create()
                    if rel[3] == 'endereco':
                        ponto.endereco = _relation_data

                    elif rel[3] == 'doc_identificacao':
                        ponto.doc_identificacao = _relation_data
                    ponto.save()
                else:
                    _field = rel[2]
                    _relation_data = rel_list[0].objects.create(**_field)

                    if rel[3] == 'endereco':
                        ponto.endereco = _relation_data

                    elif rel[3] == 'doc_identificacao':
                        ponto.doc_identificacao = _relation_data
                    ponto.save()

            return ponto

    def create(self, validated_data):

        _field_many_to_many = ['atracoes', 'comentarios', 'avaliacoes']
        _field_one_to_one = ['endereco', 'doc_identificacao']

        ponto = PontoTuristicos

        _data_many = []
        _data_one = []

        for many_to_many in _field_many_to_many:
            _data_many.append(validated_data[many_to_many])
            del validated_data[many_to_many]

        if _field_one_to_one.__len__() > 1:
            ponto = self.create_relations_one_to_one(_field_one_to_one, validated_data)
        else:
            endereco = validated_data[str(_field_one_to_one[0])]
            del validated_data[str(_field_one_to_one[0])]
            one_to_one_model_field = Endereco.objects.create(**endereco)
            ponto = ponto.objects.create(**validated_data)
            ponto.endereco = one_to_one_model_field
            ponto.save()

        self.create_relations_many_to_many(ponto, _data_many)
        return ponto




