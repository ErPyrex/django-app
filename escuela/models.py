from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre + " " + self.apellido