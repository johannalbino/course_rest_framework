from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from enderecos.models import Endereco
from type_test.models import TypeTest

# Create your models here.


class DocIdentificacao(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        managed = True


class PontoTuristicos(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    type1 = models.ForeignKey(TypeTest, related_name='type1', on_delete=models.PROTECT, null=True, blank=True)
    type2 = models.ForeignKey(TypeTest, related_name='type2', on_delete=models.PROTECT, null=True, blank=True)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'pontos_turisticos'

    def __str__(self):
        return self.name

