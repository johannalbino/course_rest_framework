from django.db import models

# Create your models here.


class atracoes(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.name