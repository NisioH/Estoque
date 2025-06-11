from django.urls import path
from .views import listar_mercadorias, cadastrar_mercadoria

urlpatterns = [
    path('listar/', listar_mercadorias, name='listar_mercadorias'),
    path('cadastrar/', cadastrar_mercadoria, name='cadastrar_mercadoria'),
]