import uuid

from django.db import models
from django.forms import DecimalField

class Produtos(models.Model):
    cod_produto = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        null=False,
        unique=True,
        blank=False
    )
    unidade = models.CharField('Unidade', max_length=10, null=False, blank=False)
    valor_unitario = models.DecimalField(
        'Valor Unitário',
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )
    descricao_produto = models.TextField('Descrição do produto', max_length=30)
    estoque_minimo = models.DecimalField('Estoque mínimo', max_digits=5, decimal_places=2)
    qtde_estoque = models.DecimalField(
        'Quantidade em estoque',
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )
