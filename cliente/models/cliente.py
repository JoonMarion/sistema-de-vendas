import email
import uuid
import uuid

from django.db import models
from django.forms import DecimalField
from cpf_field.models import CPFField

class Cliente(models.Model):
    cod_cliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, unique=True, blank=False)
    cpf = models.CPFField('CPF', max_length=11, unique=True)
    nome_cliente = models.CharField('Nome', max_length=255, null=False)
    renda = models.DecimalField('Renda', max_digits=5, decimal_places=2)
    email = models.EmailField('Email', max_length=255, null=False)
    classe = models.TextField('Classe', max_length=255, null=False)
