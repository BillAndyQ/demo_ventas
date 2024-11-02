from django.contrib import admin
from .models import Negocios, NegociosUsers
# Register your models here.

# Registra el modelo Departamento
admin.site.register(Negocios)
admin.site.register(NegociosUsers)