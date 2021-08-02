from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Perfiles, Comentarios_publicacion, Categorias, Articulos

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Perfiles)
admin.site.register(Comentarios_publicacion)
admin.site.register(Categorias)
admin.site.register(Articulos)
