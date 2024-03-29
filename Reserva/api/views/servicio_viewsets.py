from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from Reserva.api.serializers.servicio_serializers import *

class ServicioViewSet(viewsets.ModelViewSet):
    serializer_class = ServicioReservaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        servicio_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(servicio_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Servicio creada correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            servicio_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if servicio_serializer.is_valid():
                servicio_serializer.save()
                return Response(servicio_serializer.data, status=status.HTTP_200_OK)
            return Response(servicio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        servicio = self.get_queryset().filter(id=pk).first()
        if servicio:
            servicio.state = False
            servicio.save()
            return Response({'message': 'Servicio Eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un servicio con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
