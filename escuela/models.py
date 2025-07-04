from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='asignaturas')

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    asignaturas = models.ManyToManyField(Asignatura, through='Inscripcion')

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'asignatura')

    def __str__(self):
        return f'{self.estudiante} inscrito en {self.asignatura}'
