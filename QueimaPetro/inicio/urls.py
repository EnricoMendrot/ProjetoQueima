from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path("", views.telainicial, name = 'telainicial'),
    path("login", views.tela_login, name = 'telalogin'),
]