from django.urls import path
from . import views

app_name = 'equipamento'
urlpatterns = [
    path("", views.exibicaoequipamento),
    path("cadastrar/", views.cadastroequipamento),
]