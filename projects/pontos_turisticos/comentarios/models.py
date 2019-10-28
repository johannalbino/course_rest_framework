from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comentarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'comentarios'

    def __str__(self):
        return self.comentario
