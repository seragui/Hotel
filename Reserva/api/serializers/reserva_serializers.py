from Reserva.models import Reserva
from rest_framework import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')