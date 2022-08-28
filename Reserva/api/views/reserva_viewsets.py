from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from Reserva.api.serializers.reserva_serializers import *

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        reserva_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(reserva_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Reserva creada correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            reserva_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if reserva_serializer.is_valid():
                reserva_serializer.save()
                return Response(reserva_serializer.data, status=status.HTTP_200_OK)
            return Response(reserva_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        reserva = self.get_queryset().filter(id=pk).first()
        if reserva:
            reserva.state = False
            reserva.save()
            return Response({'message': 'Reserva Eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una reserva con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
