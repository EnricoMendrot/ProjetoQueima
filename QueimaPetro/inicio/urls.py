from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path("", views.tela_inicial, name = 'telainicial'),
    path("login/", views.tela_login, name = 'telalogin'),
    path("senha/", views.tela_senha, name = 'telasenha'),
]