from rest_framework.routers import DefaultRouter
from Reserva.api.views.reserva_viewsets import *

router=DefaultRouter()

router.register(r'reserva',ReservaViewSet, basename='rserva')
urlpatterns=router.urls