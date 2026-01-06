from django.shortcuts import render, redirect, get_object_or_404
from database.models import Equipamento
# Create your views here.

# ========= VISUALIZAÇÃO ================= #

def telainicial(request):
    return render(request, 'index.html')