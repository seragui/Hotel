from Reserva.models import ServiciosReserva
from rest_framework import serializers


class ServicioReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosReserva
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')