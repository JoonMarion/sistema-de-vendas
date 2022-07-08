# Generated by Django 4.0.4 on 2022-07-08 03:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('cod_produto', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('unidade', models.CharField(max_length=10, verbose_name='Unidade')),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor Unitário')),
                ('descricao_produto', models.TextField(max_length=30, verbose_name='Descrição do produto')),
                ('estoque_minimo', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Estoque mínimo')),
                ('qtde_estoque', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Quantidade em estoque')),
            ],
        ),
    ]
