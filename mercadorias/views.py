from django.shortcuts import render, redirect
from .models import Mercadoria
from .forms import MercadoriaForm

def listar_mercadorias(request):
    mercadorias = Mercadoria.objects.all()
    return render(request, "mercadorias/listar.html", {"mercadorias": mercadorias})

def cadastrar_mercadoria(request):
    form = MercadoriaForm()
    if request.method == "POST":
        form = MercadoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mercadorias')
        else:
            form = MercadoriaForm()

    return render(request, 'mercadorias/cadastrar.html', {'form': form})