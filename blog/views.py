from django.shortcuts import render, redirect
from blog.forms import ArtForm, BuscarArtForm, ComForm, ContactoForm
from blog.models import Articulo, Comentario, Mensaje
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def inicio(request):  # Home de la web en general.
    return render(request, "base.html")


def about_me(request):  # Acerca de mí, accesible desde la interfaz.
    return render(request, "about.html")

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            form_save = Mensaje(nombre =info["nombre"],
                                 email =info["email"],
                                 mensaje =info["mensaje"],
                                 )
            form_save.save()            
            return redirect("gracias")  # Redirige a una página de agradecimiento
    
    form = ContactoForm()
    contexto = {"form": form}
    return render(request, 'contacto.html', context=contexto)

def gracias(request): #Agradecimiento luego de enviar un formulario de contacto
    return render(request, "gracias.html")


@login_required
def crear_blog(request):  # Esta vista permite que cada usuario publique los blog que quiera.

    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES)

        if form.is_valid():
            info = form.cleaned_data
            form_save = Articulo(fecha=info["fecha"],
                                 titulo=info["titulo"],
                                 subtitulo=info["subtitulo"],
                                 cuerpo=info["cuerpo"],
                                 imagen=info["imagen"],
                                 autor=request.user)
            form_save.save()
            return redirect("inicio")

    form = ArtForm()
    contexto = {"form": form}
    return render(request, "blog/creacion.html", context=contexto)


@login_required
def edit_art(request, titulo):  # Esta vista permite que cada usuario pueda editar su artículo.
    art = Articulo.objects.get(titulo=titulo)

    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES)

        if form.is_valid():
            info = form.cleaned_data

            art.titulo = info["titulo"]
            art.subtitulo = info["subtitulo"]
            art.cuerpo = info["cuerpo"]
            art.imagen = info["imagen"]

            art.save()
            return redirect("inicio")
        else:
            messages.warning(request, "No se pudo editar el artículo.")

    form = ArtForm(initial={
        "titulo": art.titulo,
        "subtitulo": art.subtitulo,
        "cuerpo": art.cuerpo,
        "imagen": art.imagen,
    })
    contexto = {"form": form, "titulo": art.titulo}

    return render(request, "blog/editart.html", context=contexto)


@login_required
def borrar_art(request, titulo):  # Esta vista permite que el usuario registrado elimine sus publicaciones.
    art = Articulo.objects.get(titulo=titulo)
    art.delete()
    return redirect("articulos")


@login_required
def det_blog(request, titulo):  # Esta vista permite acceder al detalle de cada artículo publicado.
    all_arts = Articulo.objects.get(titulo=titulo)
    contexto = {"titulo": all_arts.titulo,
                "subtitulo": all_arts.subtitulo,
                "cuerpo": all_arts.cuerpo,
                "imagen": all_arts.imagen,
                "autor": all_arts.autor,
                "fecha": all_arts.fecha,
                "form_busqueda": BuscarArtForm(),
                }
    return render(request, "blog/articulo.html", context=contexto)


@login_required
def articulos(request):  # Esta vista permite que cada usuario vea que blog hay publicados hasta el momento.
    all_arts = Articulo.objects.all()
    contexto = {"all_arts": all_arts, "form_busqueda": BuscarArtForm()}
    return render(request, "blog/detalle.html", context=contexto)


@login_required
def buscar_art(request):  # Esta vista permite que el usuario busque el trago que quiera a través de la interfaz.
    form = BuscarArtForm(request.GET)

    if form.is_valid():
        info = form.cleaned_data
        filtro = Articulo.objects.filter(titulo__icontains=info["titulo"])
        contexto = {"filtro": filtro}
        return render(request, "blog/resultados_busqueda.html", context=contexto)


@login_required
def coment_art(request):  # Esta vista permite que un usuario comente el artículo que quiera.

    if request.method == "POST":
        form = ComForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            form_save = Comentario(date=info["date"],
                                   titulo=info["titulo"],
                                   comentar=info["comentar"],
                                   articulo=info["articulo"],
                                   author=request.user)
            form_save.save()
            return redirect("articulos")

    form = ComForm()
    contexto = {"form": form}
    return render(request, "blog/comentart.html", context=contexto)


@login_required
def mostrar_com(request, titulo):  # Esta vista permite listar los comentarios a cada artículo en particular.
    articulos = Articulo.objects.get(titulo=titulo)
    art_id = articulos.id
    com = Comentario.objects.filter(articulo_id=art_id)
    contexto = {"comentarios": com, "titulo": articulos}
    return render(request, "blog/mostrarCom.html", context=contexto)
