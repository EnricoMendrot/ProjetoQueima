from django.urls import path, include
from . import views

app_name = 'operadores'
urlpatterns = [
    path("", views.visualizar_operadores, name= 'visualizacao'),
    path("cadastrar/",views.cadastro_operadores, name= 'cadastro'),
]