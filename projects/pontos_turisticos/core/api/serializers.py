from rest_framework import serializers
from core.models import PontoTuristicos, Atracoes, Comentarios, Endereco, Avaliacoes
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicosSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)


    class Meta:
        model = PontoTuristicos
        fields = ('id', 'name', 'description', 'aprovado', 'photo', 'atracoes', 'comentarios', 'avaliacoes', 'endereco')
        read_only_fields = ('comentarios', 'avaliacoes', 'endereco')

    def create_relations_many_to_many(self, ponto, *args, **kwargs):
        models = [Atracoes, Comentarios, Avaliacoes]
        campos_pk = [ponto.atracoes, ponto.comentarios, ponto.avaliacoes]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                at = rel[0].objects.create(**rel[2][0])
                rel[1].add(at)

    def create_relations_one_to_one(self, ponto, *args, **kwargs):
        models = [Endereco]
        campos_pk = [ponto.endereco]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                at = rel[0].objects.create(**rel[2])
                rel[1] = at
                ponto.save()

    def create(self, validated_data):

        _field_many_to_many = ['atracoes', 'comentarios', 'avaliacoes']
        _field_one_to_one = ['endereco']

        ponto = PontoTuristicos

        _data_many = []
        _data_one = []

        for many_to_many in _field_many_to_many:
            _data_many.append(validated_data[many_to_many])
            del validated_data[many_to_many]

        if _field_one_to_one.__len__() > 1:
            for one_to_one in _field_one_to_one:
                _data_one.append(validated_data[one_to_one])
                del validated_data[one_to_one]

            ponto = PontoTuristicos.objects.create(**validated_data)
            self.create_relations_one_to_one(ponto, _data_one)
            ponto.save()
        else:
            endereco = validated_data[str(_field_one_to_one[0])]
            del validated_data[str(_field_one_to_one[0])]
            one_to_one_model_field = Endereco.objects.create(**endereco)
            ponto = ponto.objects.create(**validated_data)
            ponto.endereco = one_to_one_model_field
            ponto.save()

        self.create_relations_many_to_many(ponto, _data_many)
        return ponto


