from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstadioViewSet, ClubViewSet, TecnicoViewSet, JugadorViewSet

router = DefaultRouter()
router.register(r'estadios', EstadioViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'tecnicos', TecnicoViewSet)
router.register(r'jugadores', JugadorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
