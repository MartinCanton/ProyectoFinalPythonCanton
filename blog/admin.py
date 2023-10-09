from django.contrib import admin
from blog.models import Articulo, Comentario, Mensaje

admin.site.register(Articulo)
admin.site.register(Comentario)
admin.site.register(Mensaje)