from django.shortcuts import render
from .models import Mercadoria

def listar_mercadoria(request):
    mercadorias = Mercadoria.objects.all()
    return render(request, "mercadorias/listar.html", {"mercadorias": mercadorias})
