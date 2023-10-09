from django.urls import path
from blog.views import inicio, crear_blog, articulos, edit_art, borrar_art, det_blog, buscar_art, about_me, coment_art, mostrar_com, contacto, gracias

urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear/", crear_blog, name="crearblog"),
    path("articulos/", articulos, name="articulos"),
    path("editart/<titulo>/", edit_art, name="editart"),
    path("borrart/<titulo>/", borrar_art, name="borrart"),
    path("detalle/<titulo>/", det_blog, name="detblog"),
    path("mostrarcom/<titulo>/", mostrar_com, name="mostrarcom"),
    path("buscart/", buscar_art, name="buscart"),
    path("about/", about_me, name="about"),
    path("comentart/", coment_art, name="comentart"),
    path('contacto/', contacto, name='contacto'),
    path('gracias/', gracias, name="gracias"),
    ]