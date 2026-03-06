from django.shortcuts import render, redirect, get_object_or_404
from .forms import EquipamentoForm
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import permission_required, login_required
from database.models import Equipamento
# Create your views here.

# ========= VISUALIZAÇÃO ================= #
@permission_required('database.view_equipamento')
def exibicaoequipamento(request):
    queryset = Equipamento.objects.all()

    # Pegar os valores dos filtros (GET)w
    nome = request.GET.get('nome', '').strip()
    status = request.GET.get('status', '').strip()
    id_eq = request.GET.get('id', '').strip()
    codigo = request.GET.get('codigo', '').strip()

    # Aplicar filtros apenas se o campo tiver valor
    if nome:
        queryset = queryset.filter(nome__icontains=nome)

    if status:
        queryset = queryset.filter(status_operacional=status)

    if id_eq:
        try:
            id_int = int(id_eq)
            queryset = queryset.filter(id=id_int)
        except ValueError:
            pass  # ignora se não for número válido

    if codigo:
        queryset = queryset.filter(codigo__icontains=codigo)

    # Ordenar (opcional, mas recomendado)
    queryset = queryset.order_by('id')

    contexto = {
        'equipamento': queryset,
    }
    return render(request, 'Visualizacao/equipamento_cadastrados.html', contexto)

# ======== Exibição do Equipamento por ID ======== #
@permission_required('database.view_equipamento')
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
@permission_required('database.change_equipamento')
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
@permission_required('database.add_equipamento')
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

    return render(request, "Cadastro/cadastro_equipamento.html", {'form': form})