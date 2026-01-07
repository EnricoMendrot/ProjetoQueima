from django.urls import path
from . import views

app_name = 'equipamento'

urlpatterns = [
    path("", views.exibicaoequipamento, name = 'visualizacao'),
    path("cadastrar/", views.cadastroequipamento, name='cadastro'),
    path("<int:ID_Equipamento>/", views.exibicaoequipamentoID, name='visualizacaoid'),
    path("editar/<int:ID_Equipamento>/", views.editar_equipamento, name='editar'),
]