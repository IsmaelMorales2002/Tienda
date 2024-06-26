# Generated by Django 5.0.6 on 2024-06-17 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='id',
        ),
        migrations.AlterField(
            model_name='pago',
            name='idPago',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id Pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total Pago'),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id Carrito')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total Carrito')),
                ('correo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Tienda.usuario', verbose_name='Correo Usuario')),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
                'db_table': 'Carro',
            },
        ),
    ]
