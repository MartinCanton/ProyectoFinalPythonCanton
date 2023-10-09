from django.urls import path
from users.views import login_user, registro, editar_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_user, name="login"),
    path('signup/', registro, name="signup"),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name="logout"), 
    path('editar/', editar_user, name="editar"),
    ]