from django.db import models
from atracoes.models import atracoes

# Create your models here.


class PontoTuristicos(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(atracoes)

    def __str__(self):
        return self.name

