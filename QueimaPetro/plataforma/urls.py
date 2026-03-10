from django.urls import path, include
from . import views

app_name = "plataforma"

urlpatterns = [
    path("", views.home, name="home"),
    path("detalhado/", views.visualizacao_grafico, name="detalhado"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("visualizar/", views.visualizar_plataforma, name="visualizar"),
    path("<int:id>/", views.visualizar_plataformaid, name="visualizacaoid"),
    path("editar/<int:id>/", views.editar_plataforma, name="editar"),
]
