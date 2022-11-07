from rest_framework.routers import DefaultRouter
from habitacion.api.views.habitacion_viewsets import *
from habitacion.api.views.caracteristica_view import *

router=DefaultRouter()

router.register(r'habitacion',HabitacionViewSet, basename='habitacion')
router.register(r'caracteristica',CaracteristicaViewSet, basename='caracteristica_habitacion')
router.register(r'disponibilidad', HabitacionReservada, basename='disponibilidad')
urlpatterns=router.urls