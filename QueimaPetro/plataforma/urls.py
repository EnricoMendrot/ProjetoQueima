from django.urls import path, include
from . import views
 
app_name = 'plataforma'

urlpatterns = [
    path("", views.visualizacao_grafico, name = 'home'),
    path("cadastrar/", views.cadastrar, name = "cadastrar"),
    path("<int:ID_Plataforma>/", views.visualizar_plataforma, name = "visualizar"),
]