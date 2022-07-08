from django import forms
from produto.models.produtos import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('unidade', 'valor_unitario', 'descricao_produto', 'estoque_minimo', 'qtde_estoque')