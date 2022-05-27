# Generated by Django 4.0.3 on 2022-05-25 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre_caracteristica', models.CharField(max_length=50, unique=True, verbose_name='Caracterisiticas')),
            ],
            options={
                'verbose_name': 'Caracteristica',
                'verbose_name_plural': 'Caracteristicas',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('tipo_habitacion', models.CharField(max_length=100, verbose_name='Tipo de Habitación')),
                ('descripcion_habitacion', models.TextField(default='Escribir descripción', max_length=500, verbose_name='Descripción de habitación')),
                ('numero_habitacion', models.IntegerField(verbose_name='Número de Habitación')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('numero_piso', models.IntegerField(verbose_name='Número de Piso')),
                ('estado_habitacion', models.BooleanField(default=False, verbose_name='Estado Habitación')),
                ('caracteristica', models.ManyToManyField(to='habitacion.caracteristica')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
    ]
