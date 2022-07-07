import uuid

from django.db import models
from django.forms import DecimalField

class Produtos(models.Model):
    cod_produto = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, unique=True)
    unidade = models.CharField(max_length=100)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    qtde_estoque = models.DecimalField(max_digits=10, decimal_places=2)
