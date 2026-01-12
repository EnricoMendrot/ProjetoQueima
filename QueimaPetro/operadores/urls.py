from django.urls import path
from . import views

app_name = 'operadores'
urlpatterns = [
    path("", views.visualizar_operadores, name= 'visualizacao'),
    path("cadastrar/",views.cadastro_operadores, name= 'cadastro'),
    path("<int:ID_Funcionario>/",views.visualizarid_operador, name= 'visualizacaoid'),
    path("editar/<int:ID_Funcionario>/",views.editar_operador, name= 'editar'),
]