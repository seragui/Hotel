from django.db import models
from base.models import BaseModel
from .models import *
from servicios.models import *
from habitacion.models import *
# Create your models here.


class Reserva(BaseModel):
    fecha_ingreso = models.DateField(
        "Fecha de ingreso", auto_now=False, auto_now_add=False)
    fecha_salida = models.DateField(
        "Fecha de salida", auto_now=False, auto_now_add=False)
    hora_ingreso = models.CharField(
        "Hora de ingreso", max_length=10)
    hora_salida = models.CharField("Hora de salida", max_length=10)
    numero_personas = models.IntegerField("Número de Personas" )
    nombre_completo = models.CharField(
        "Nombre completo de Cliente", max_length=200)
    documento_identidad = models.CharField("Documento de Identidad", max_length=12, default="")
    direccion = models.CharField("Direccion de Cliente",max_length=40, default="")
    numero_contacto = models.CharField(
        "Numero de contacto", max_length=12)
    email = models.EmailField("Email")
    id_habitacion = models.ForeignKey(
        "habitacion.Habitacion", on_delete=models.CASCADE)
    id_servicio = models.ManyToManyField(
        "ServiciosReserva")

    class Meta:
        verbose_name = ('Reserva')
        verbose_name_plural = ('Reservas')


class ServiciosReserva(BaseModel):
    nombre_servicio = models.CharField(
        'Nombre de Servicio',  max_length=100, blank=False)
    descripcion = models.TextField('Descripción', blank=False)
    precio = models.FloatField('Precio', blank=False)
    capacidad = models.CharField(
        'Capacidad', max_length=50, blank=False,default='')

    class Meta:
        verbose_name = ('Servicio')
        verbose_name_plural = ('Servicios')

    def __str__(self):
        return self.nombre_servicio
