import uuid

from cliente import models as cliente_models
from django.db import models
from django.forms import DecimalField

class Vendas(models.Model):
    cod_venda = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        null=False,
        unique=True,
        blank=False
    )
    cod_cliente = models.ForeignKey('cliente_models.Clientes')
    data_venda = models.DateField('Data da venda', null=False, blank=False)