import email
import uuid
import uuid

from django.db import models
from django.forms import DecimalField

class Cliente(models.Model):

    CLASSE_ESCOLHA = [
        ('Classe AB', 'Classe AB - renda domiciliar per capita acima de R$ 4591'),
        ('Classe C', 'Classe C - renda domiciliar entre R$ 1064 e R$ 4591'),
        ('Classe D', 'Classe D - renda domiciliar entre R$ 768 e R$ 1064'),
        ('Classe E', 'Classe E - renda domiciliar até R$ 768'),
    ]

    cod_cliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, unique=True, blank=False)
    cpf = models.CharField(max_length=11, null=False, unique=True, blank=False)
    nome_cliente = models.CharField('Nome', max_length=255, null=False)
    renda = models.DecimalField('Renda', max_digits=5, decimal_places=2)
    email = models.EmailField('Email', max_length=255, null=False)
    classe = models.CharField(max_length=50, choices=CLASSE_ESCOLHA)
