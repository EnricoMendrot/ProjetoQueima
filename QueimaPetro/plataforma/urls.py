from django.urls import path, include
from . import views
 
app_name = 'plataforma'

urlpatterns = [
    path("", views.visualizacao_grafico, name = 'home'),
    path("cadastrar/", views.cadastrar, name = "cadastrar"),
    path("visualizar/", views.visualizar_plataforma, name = "visualizar"),
    path("<int:id>/", views.visualizar_plataformaid, name = "visualizacaoid"), 
    path("editar/<int:id>/", views.editar_plataforma, name = "editar"), 
]