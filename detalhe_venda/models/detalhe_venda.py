import email
import uuid

from venda import models as venda_models
from produto import models as produto_models
from django.db import models
from django.forms import DecimalField
from cpf_field.models import CPFField

class DetalheVenda(models.Model):
    cod_produto = models.ForeignKey('produto_models.Produtos', primary_key=True)
    cod_venda = models.ForeignKey('venda_models.Vendas', primary_key=True)
    qtd_produto =  models.DecimalField(
        'Quantidade do produto relacionado',
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )