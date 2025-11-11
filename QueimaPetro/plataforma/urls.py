from django.urls import path, include
from . import views
 
app_name = 'plataforma'

urlpatterns = [
    path("", views.visualizacao_grafico, name = 'visualizacao')
]