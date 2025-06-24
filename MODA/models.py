from django.db import models

class Lacouturière(models.Model):
    nombre_local = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    descripcion = models.TextField()
    puntuacion = models.IntegerField()  # de 1 a 5
    fecha_visita = models.DateField()
    reseñador = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes_marcas/', null=True, blank=True)
    
    # En vez de precio exacto, usamos accesibilidad
    precio_accesible = models.BooleanField(default=True)  # True = Accesible, False = No accesible

    def __str__(self):
        return f"{self.nombre_local} ({self.puntuacion}/5)"
