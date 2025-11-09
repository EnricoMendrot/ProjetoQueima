from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import EquipamentoForm
# Create your views here.

def exibicaoequipamento(request):
    return HttpResponse("Olá")

def cadastroequipamento(request):
    if request.method == "POST":
        formulario = EquipamentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("operadores:visualizacao")
        
    contexto = {
        'form': EquipamentoForm
    }
    return render(request,"Cadastro/CadastroEquipamento.html", contexto)