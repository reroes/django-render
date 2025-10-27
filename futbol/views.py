from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Club, Estadio, Tecnico, Jugador
from .serializers import ClubSerializer, EstadioSerializer, TecnicoSerializer, JugadorSerializer

class EstadioViewSet(viewsets.ModelViewSet):
    queryset = Estadio.objects.all()
    serializer_class = EstadioSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

