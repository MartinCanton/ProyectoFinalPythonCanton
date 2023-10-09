from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserRegisterForm, UserEditForm
from users.models import Avatar
from django.contrib import messages


def login_user(request):  # Vista del LOG IN --> Para que el usuario inicie sesión.

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(username=info["username"], password=info["password"])

            if user:
                login(request, user)
                return redirect("inicio")
        else:
            messages.warning(request, "El usuario o la contraseña son incorrectos.")

    form = AuthenticationForm()
    contexto = {"form": form}
    return render(request, "users/login.html", context=contexto)


def registro(request):  # Vista de SIGN UP --> Para que un usuario se registre.
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        else:
           # Agregar mensajes de error al contexto para mostrarlos en el template
            errores = form.errors.values()
            for error in errores:
                messages.error(request, error)

            messages.warning(request, "No se pudo registrar el usuario.")

    form = UserRegisterForm()
    contexto = {"form": form}
    return render(request, "users/registro.html", context=contexto)


@login_required
def editar_user(request):  # Vista para que un usuario edite su perfil. Si o si debe de estar logueado.

    user = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)

        if form.is_valid():
            informacion = form.cleaned_data

            
            user.first_name = informacion["first_name"]
            user.last_name = informacion["last_name"]
            user.email = informacion["email"]

            try:
                user.avatar.imagen = informacion["imagen"]
                user.avatar.save()
            except:
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()

            user.save()
            return render(request, "base.html")
        else:
            # Aquí obtenemos los errores del formulario y los pasamos al contexto
            errors = form.errors.as_data()
            context = {"form": form, "nombre": user.first_name, "errors": errors}
            messages.warning(request, "No se pudo editar el usuario. Revise los datos ingresados.")
            return render(request, "users/edicion.html", context=context)

    form = UserEditForm(initial={
        
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    })

    context = {"form": form, "nombre": user.first_name}
    return render(request, "users/edicion.html", context=context)