from rest_framework.routers import DefaultRouter
from Reserva.api.views.reserva_viewsets import *
from Reserva.api.views.servicio_viewsets import *

router=DefaultRouter()

router.register(r'reserva',ReservaViewSet, basename='reserva')
router.register(r'servicio',ServicioViewSet, basename='servicio')
urlpatterns=router.urls