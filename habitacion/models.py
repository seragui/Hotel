from django.db import models
from base.models import BaseModel

# Create your models here.


class Habitacion(BaseModel):
    tipo_habitacion = models.CharField(
        "Tipo de Habitación", max_length=100, blank=False )
    descripcion_habitacion = models.TextField(
        'Descripción de habitación', max_length=500 , default='Escribir descripción')
    numero_habitacion = models.IntegerField(
        'Número de Habitación', blank=False )
    precio = models.DecimalField(
        'Precio', max_digits=6, decimal_places=2, blank=False )
    numero_piso = models.IntegerField(
        'Número de Piso', blank=False )
    estado_habitacion = models.BooleanField(
        'Estado Habitación', blank=False , default=False)
    caracteristica = models.ManyToManyField("Caracteristica")
    imagen_habitacion = models.ImageField(
        'Imagen de Habitación', upload_to=None, height_field=None, width_field=None, max_length=None, default=' ')

    class Meta:
        verbose_name = ('Habitacion')
        verbose_name_plural = ('Habitaciones')

    def __str__(self):
        id_habitacion= str(self.id)
        return id_habitacion


class Caracteristica(BaseModel):
    nombre_caracteristica = models.CharField(
        'Caracterisiticas', max_length=50, blank=False , unique=True)

    class Meta:
        verbose_name = ('Caracteristica')
        verbose_name_plural = ('Caracteristicas')

    def __str__(self):
        return self.nombre_caracteristica
