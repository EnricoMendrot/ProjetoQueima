from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from database.models import Funcionario
from .forms import CadastroOperador

# Create your views here.

def visualizar_operadores(request):
    contexto = {
        "funcionario": Funcionario.objects.all()
    }

    return render(request, "Operadores/ListaOperador.html", contexto)

def criar_operadores(request):
    # Para criar um metodo POST
    if request.method == "POST":
        formulario = CadastroOperador(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("operadores:visualizacao")
        
    contexto = {
        "form":  CadastroOperador
    }
    return render(request, "Operadores/Cadastro.html", contexto)