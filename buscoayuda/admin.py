from django.contrib import admin
from buscoayuda.models import TiposDeServicio
from buscoayuda.models import Trabajador
from buscoayuda.models import Comentario

admin.site.register(TiposDeServicio)
admin.site.register(Trabajador)
admin.site.register(Comentario)