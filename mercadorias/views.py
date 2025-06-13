from django.shortcuts import render, redirect, get_object_or_404
from .models import Mercadoria
from .forms import MercadoriaForm

def listar_mercadorias(request):
    mercadorias = Mercadoria.objects.all()
    return render(request, "mercadorias/listar.html",
                  {"mercadorias": mercadorias})

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


# def atualizar_mercadoria(request, mercadoria_id):
#     mercadoria = get_object_or_404(Mercadoria, id=mercadoria_id)  # ✅ Garantindo que o ID existe
#
#     if request.method == "POST":
#         form = MercadoriaForm(request.POST, instance=mercadoria)
#         if form.is_valid():
#             form.save()
#             return redirect("listar_mercadorias")  # ✅ Sempre retorna um HttpResponse
#     else:
#         form = MercadoriaForm(instance=mercadoria)  # ✅ Preenche o form com os dados atuais
#
#     return render(request, "mercadorias/atualizar.html",
#                   {"form": form, "mercadoria": mercadoria})  # ✅ Sempre retorna um HttpResponse


def atualizar_mercadoria(request, mercadoria_id):
    mercadoria = get_object_or_404(Mercadoria, id=mercadoria_id)  # ✅ Certifica que o ID é válido

    if request.method == "POST":
        form = MercadoriaForm(request.POST, instance=mercadoria)
        if form.is_valid():
            form.save()
            return redirect("listar_mercadorias")  # ✅ Redireciona após salvar
    else:
        form = MercadoriaForm(instance=mercadoria)  # ✅ Preenche com os dados atuais

    return render(request, "mercadorias/atualizar.html",
                  {"form": form, "mercadoria": mercadoria})  # ✅ Passa o formulário para o template
