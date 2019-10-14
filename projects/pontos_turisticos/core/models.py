from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from enderecos.models import Endereco

# Create your models here.


class PontoTuristicos(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.name

