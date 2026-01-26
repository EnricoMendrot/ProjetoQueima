from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from database.models import Funcionario
from django.http import HttpRequest
from .forms import OperadorForm

# ========================== Visualização ========================== #

def visualizar_operadores(request):
    queryset=Funcionario.objects.all()
    # Pegar os valores dos filtros (GET)
    nome = request.GET.get('nome', '').strip()
    setor = request.GET.get('setor', '').strip()
    id_op = request.GET.get('id', '').strip()
    turno = request.GET.get('turno', '').strip()

    # Aplicar filtros apenas se o campo tiver valor
    if nome:
        queryset = queryset.filter(nome__icontains=nome)

    if setor:
        queryset = queryset.filter(setor=setor)

    if id_op:
        try:
            id_int = int(id_op)
            queryset = queryset.filter(id=id_int)
        except ValueError:
            pass  # ignora se não for número válido

    if turno:
        queryset = queryset.filter(turno__icontains=turno)

    # Ordenar (opcional, mas recomendado)
    queryset = queryset.order_by('id')

    contexto = {
        "funcionario": queryset,
    }


    return render(request, "Visualizacao/operadores_cadastrados.html", contexto)

# =================== Visualização por ID ======================= #

def visualizarid_operador (request, id):
    try:
        funcionario = Funcionario.objects.get(id = id)
    except Funcionario.DoesNotExist:
        messages.error(request, f"Funcionario com o ID {id} não existe")

    contexto = {
        "funcionario": funcionario
    }
    return render(request, "VisualizacaoID_Operador/index.html", contexto)

# =================== Editar por ID ======================= #

def editar_operador(request:HttpRequest, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        form = OperadorForm(request.POST, instance=funcionario)
        
        if form.is_valid():
            form.save()
            return redirect("operadores:visualizacaoid", id=funcionario.id)
        
    form = OperadorForm(instance=funcionario)
    context = {
        'form': form,
        'funcionario': funcionario
    }
    return render(request, 'VisualizacaoID_Operador/index_editar.html',context)
# ========================== CADASTRO ========================== #
def cadastro_operadores(request):
    if request.method == "POST":
        form = OperadorForm(request.POST)
        
        if form.is_valid():
            form.save()
            print("Formulário válido e salvo com sucesso!")
            return redirect("operadores:visualizacao")
        
        else:
            print("Formulário INVÁLIDO!")
            print(form.errors)
    
    else:
        form = OperadorForm()

    return render(request, "Cadastro/CadastroOperador.html", {"form": form})