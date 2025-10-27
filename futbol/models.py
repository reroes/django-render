from django.db import models

class Estadio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Club(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()
    estadio = models.ForeignKey(Estadio, on_delete=models.SET_NULL, null=True, blank=True, related_name="clubs")

    def __str__(self):
        return self.nombre

class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=50)  # Nuevo campo para tipo de técnico
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="tecnicos")

    def __str__(self):
        return f"{self.nombre} ({self.rol})"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return self.nombre
