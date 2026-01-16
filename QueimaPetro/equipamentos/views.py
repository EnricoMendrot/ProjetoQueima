from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipamentoForm
from django.contrib import messages
from django.http import HttpRequest
from database.models import Equipamento
# Create your views here.

# ========= VISUALIZAÇÃO ================= #

def exibicaoequipamento(request):
    contexto = {
        "equipamento": Equipamento.objects.all()
    }
    return render(request, 'Visualizacao/VisualizacaoEquipamento.html', contexto)

# ======== Exibição do Equipamento por ID ======== #
def exibicaoequipamentoID(request, id):
    # equipamento = get_object_or_404(Equipamento, id=id)
    
    try:
        equipamento = Equipamento.objects.get(id = id)
    except Equipamento.DoesNotExist:
        messages.error(request, f"Equipamento com o ID {id} não existe")

    contexto = {
        "equipamento": equipamento
    }
    return render(request, "VisualizacaoID/index.html", contexto)

# ===== Editar Equipamento ====== #
def editar_equipamento(request:HttpRequest, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        
        if form.is_valid:
            form.save()
            return redirect("equipamento:visualizacaoid", id=equipamento.id)
        
    form = EquipamentoForm(instance=equipamento)
    context = {
        'form': form,
        'equipamento': equipamento
    }
    return render(request, 'VisualizacaoID/index_editar.html',context)

# ===== Cadastro do Equipamento ======= #
def cadastroequipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save()
            messages.success(request, f'Equipamento "{Equipamento.nome}" cadastrado com sucesso!')
            return redirect("equipamento:visualizacao")
        else:
            print("FORMULÁRIO INVÁLIDO - NÃO SALVOU")
            messages.error(request, 'Corrija os erros abaixo antes de enviar.')

    else:
        form = EquipamentoForm()
        print("Acessando via GET - formulário vazio")

    return render(request, "Cadastro/index.html", {'form': form})