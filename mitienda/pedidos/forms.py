from django import forms
from .models import Pedido

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["nombre", "apellidos", "email","direccion","codigo_postal","ciudad"]
        
