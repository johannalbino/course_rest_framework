from django.contrib import admin
from .models import PontoTuristicos
from .models import DocIdentificacao

# Register your models here.

admin.site.register(DocIdentificacao)
admin.site.register(PontoTuristicos)
