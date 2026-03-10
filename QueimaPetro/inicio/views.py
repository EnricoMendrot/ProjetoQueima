from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from database.models import Equipamento
# Create your views here.

# ========= VISUALIZAÇÃO ================= #

def tela_inicial(request):
    return render(request, 'home/index.html')

def tela_login(request):
    # Se o formulário foi submetido (POST)
    if request.method == 'POST':
        # 1. Capture o que o usuário digitou no HTML
        # O nome do campo entre aspas DEVE ser igual ao atributo 'name' da tag <input> no seu login.html
        u = request.POST.get('username') 
        s = request.POST.get('password')
        
        # 2. Peça pro Django conferir se existe no banco de dados
        user = authenticate(request, username=u, password=s)
        
        # 3. Se ele encontrou e a senha bate (autenticado!)
        if user is not None:
            # Efetive o login na sessão
            login(request, user)
            
            # Mande ele pro painel inicial
            return redirect('plataforma:home')
            
        else:
            # Se errou, mande uma mensagem de erro e devolva a mesma tela
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login/login.html') 
            
    # Se for só um GET (abriu a página agora), só mostra o HTML
    return render(request, 'login/login.html')

def tela_senha(request):
    return render(request, "password/rec_senha.html")