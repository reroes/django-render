# Register your models here.
from django.contrib import admin
from futbol.models import Club, Estadio, Tecnico, Jugador

@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'capacidad')
    search_fields = ('nombre', 'ciudad')

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'fecha_fundacion', 'estadio')
    list_filter = ('ciudad',)
    search_fields = ('nombre',)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol', 'nacionalidad', 'club')
    list_filter = ('rol', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'club')
    list_filter = ('posicion',)
    search_fields = ('nombre',)
