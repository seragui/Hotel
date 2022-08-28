from tkinter import CASCADE
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
        "Hora de ingreso", max_length=10, null=False)
    hora_salida = models.CharField("Hora de salida", max_length=10, null=False)
    numero_personas = models.IntegerField("Número de Personas", null=False)
    nombre_completo = models.CharField(
        "Nombre completo de Cliente", max_length=200, null=False)
    numero_contacto = models.CharField(
        "Numero de contacto", max_length=12, null=False)
    email = models.EmailField("Email", null=False)
    id_servicio = models.ForeignKey(
        "servicios.Servicios", on_delete=models.CASCADE)
    id_habitacion = models.ForeignKey(
        "habitacion.Habitacion", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Reserva')
        verbose_name_plural = ('Reservas')
