from django import forms
from .models import Mercadoria

class MercadoriaForm(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = ['nome', 'quantidade', 'setor']
        widgets = {
            'setor': forms.Select(attrs={'required': False})
        }