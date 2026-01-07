from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipamentoForm
from django.contrib import messages
from database.models import Equipamento
# Create your views here.

# ========= VISUALIZAÇÃO ================= #

def exibicaoequipamento(request):
    contexto = {
        "equipamento": Equipamento.objects.all()
    }
    return render(request, 'Visualizacao/VisualizacaoEquipamento.html', contexto)

# ======== Exibição do Equipamento por ID ======== #
def exibicaoequipamentoID(request, ID_Equipamento):
    # equipamento = get_object_or_404(Equipamento, ID_Equipamento=ID_Equipamento)
    
    try:
        equipamento = Equipamento.objects.get(ID_Equipamento = ID_Equipamento)
    except Equipamento.DoesNotExist:
        messages.error(request, f"Equipamento com o ID {ID_Equipamento} não existe")

    contexto = {
        "equipamento": equipamento
    }
    return render(request, "VisualizacaoID/index.html", contexto)

# ===== Cadastro do Equipamento ======= #
def cadastroequipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        print("\n=== NOVO POST RECEBIDO ===")
        print("Dados recebidos:", request.POST)
        print("Formulário válido?", form.is_valid())
        print("Erros encontrados:", form.errors)
        print("Erros não ligados a campo:", form.non_field_errors())

        if form.is_valid():
            equipamento = form.save()
            print("SALVOU COM SUCESSO! ID:", Equipamento.pk)
            messages.success(request, f'Equipamento "{Equipamento.Nome}" cadastrado com sucesso!')
            return redirect("equipamentos:visualizacao")
        else:
            print("FORMULÁRIO INVÁLIDO - NÃO SALVOU")
            messages.error(request, 'Corrija os erros abaixo antes de enviar.')

    else:
        form = EquipamentoForm()
        print("Acessando via GET - formulário vazio")

    return render(request, "Cadastro/index.html", {'form': form})