from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipamentoForm
from database.models import Equipamento
# Create your views here.

# ========= VISUALIZAÇÃO ================= #

def exibicaoequipamento(request):
    contexto = {
        "equipamento": Equipamento.objects.all()
    }
    return render(request, 'Visualizacao/VisualizacaoEquipamento.html', contexto)

def exibicaoequipamentoID(request, ID_Equipamento):
    equipamento = get_object_or_404(Equipamento, ID_Equipamento=ID_Equipamento)
    
    contexto = {
        "equipamento": equipamento
    }
    return render(request, "VisualizacaoID/visualizacaoid.html", contexto)

def cadastroequipamento(request):
    if request.method == "POST":
        formulario = EquipamentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("equipamentos:visualizacao")  # ajuste o nome da rota se for diferente
    else:
        formulario = EquipamentoForm()

    contexto = {
        'form': formulario
    }
    return render(request, "Cadastro/index.html", contexto)