from rest_framework import serializers
from .models import Club, Estadio, Tecnico, Jugador

class EstadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadio
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    estadio = EstadioSerializer(read_only=True)

    class Meta:
        model = Club
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    club = serializers.StringRelatedField()  # Opcional: mostrar el nombre del club en vez del id

    class Meta:
        model = Tecnico
        fields = '__all__'

class JugadorSerializer(serializers.ModelSerializer):
    club = serializers.StringRelatedField()  # Opcional: mostrar el nombre del club en vez del id

    class Meta:
        model = Jugador
        fields = '__all__'
