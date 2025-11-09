from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import EquipamentoForm
from database.models import Equipamento
# Create your views here.

def exibicaoequipamento(request):
    contexto = {
        "equipamento": Equipamento.objects.all()
    }
    return render(request, 'Visualizacao/VisualizacaoEquipamento.html', contexto)

def cadastroequipamento(request):
    if request.method == "POST":
        formulario = EquipamentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("equipamentos:visualizacao")
        
    contexto = {
        'form': EquipamentoForm
    }
    return render(request,"Cadastro/CadastroEquipamento.html", contexto)