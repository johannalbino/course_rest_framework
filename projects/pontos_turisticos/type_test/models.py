from django.db import models

# Create your models here.


class TypeTest(models.Model):
    id_type_test = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.description