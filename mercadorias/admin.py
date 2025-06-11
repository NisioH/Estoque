from statistics import quantiles

from django.contrib import admin
from .models import Setor, Mercadoria

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Mercadoria)
class MercadoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'quantidade', 'setor')
    search_fields = ['nome']
    list_filter = ('setor',)

