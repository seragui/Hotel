from django.db import models
from base.models import BaseModel

# Create your models here.


class Cargo(BaseModel):

    nombre_cargo = models.CharField(
        'Nombre de Cargo', max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = ("Cargo")
        verbose_name_plural = ("Cargos")

    def __str__(self):
        return self.nombre_cargo


class Departamento(BaseModel):

    nombre_departamento = models.CharField(
        'Nombre de Departamento', max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = ('Departamento')
        verbose_name_plural = ('Departamentos')

    def __str__(self):
        return self.nombre_departamento


class Empleados(BaseModel):

    nombres = models.CharField(
        'Nombres', max_length=100, blank=False )
    apellidos = models.CharField(
        'Apellidos', max_length=100, blank=False )
    fecha_nacimiento = models.DateField(
        'Fecha de Nacimiento', auto_now=False, auto_now_add=False, blank=False )
    nacionalidad = models.CharField(
        'Nacionalidad', max_length=50, blank=False )
    dui = models.IntegerField('DUI', blank=False , unique=True)
    isss = models.IntegerField(
        'Numero de Afiliado', blank=False , unique=True)
    nup = models.IntegerField('Numero de Pensionado',
                              blank=False , unique=True)
    direccion = models.TextField(
        'Direccion', max_length=400, blank=False )
    ciudad = models.CharField('Ciudad', max_length=50, blank=False )
    telefono = models.IntegerField('Telefono', blank=False )
    sexo = models.CharField('Sexo', max_length=1)
    email = models.EmailField('Email', max_length=254, blank=False , default='email')
    fecha_contratacion = models.DateField(
        'Fecha de Contratacion', auto_now=False, auto_now_add=False, blank=False )
    id_cargo = models.ForeignKey(
        'Cargo', verbose_name='Cargo', on_delete=models.CASCADE, blank=False )
    id_departamento = models.ForeignKey(
        'Departamento', verbose_name='Departamento', on_delete=models.CASCADE, blank=False )

    class Meta:
        verbose_name = ("Empleado")
        verbose_name_plural = ("Empleados")

    def __str__(self):
        return self.nombres
