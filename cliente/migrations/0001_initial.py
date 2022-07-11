# Generated by Django 4.0.6 on 2022-07-11 02:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cod_cliente', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome_cliente', models.CharField(max_length=255, verbose_name='Nome')),
                ('renda', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Renda')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('classe', models.TextField(max_length=255, verbose_name='Classe')),
            ],
        ),
    ]