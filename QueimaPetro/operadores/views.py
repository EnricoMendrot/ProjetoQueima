from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from database.models import Funcionario
from .forms import CadastroOperador


def visualizar_operadores(request):
    contexto = {
        "funcionario": Funcionario.objects.all()
    }

    return render(request, "Operadores/ListaOperador.html", contexto)

# ========================== CADASTRO ========================== #
def cadastro_operadores(request):
    if request.method == "POST":
        form = CadastroOperador(request.POST)
        
        if form.is_valid():
            form.save()
            print("→ Formulário válido e salvo com sucesso!")
            # messages.success(request, "Operador cadastrado com sucesso!")  # opcional
            return redirect("operadores:visualizacao")
        
        else:
            print("→ Formulário INVÁLIDO!")
            print(form.errors)               # <--- importante para debug
            # NÃO crie um form novo aqui!!!
    
    else:
        # GET → formulário limpo
        form = CadastroOperador()

    # MUITO IMPORTANTE: sempre passar o mesmo form (com erros se houver)
    return render(request, "Cadastro/CadastroOperador.html", {"form": form})