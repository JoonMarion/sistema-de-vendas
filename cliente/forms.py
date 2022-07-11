from django import forms
from cliente.models.cliente import Cliente



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cpf', 'nome_cliente', 'renda', 'email', 'classe')