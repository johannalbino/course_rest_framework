from django.db import models

# Create your models here.


class Atracoes(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    photo = models.ImageField(upload_to='atracoes', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'atracoes'

    def __str__(self):
        return self.name