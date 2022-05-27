# Generated by Django 4.0.3 on 2022-05-25 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre_servicio', models.CharField(max_length=100, verbose_name='Nombre de Servicio')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('iva', models.FloatField(verbose_name='IVA')),
                ('fecha', models.DateField(verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
    ]
