from django.contrib import admin
from .models import Paciente
from .models import Medico


# Register your models here.
admin.site.register(Paciente)
admin.site.register(Medico)
