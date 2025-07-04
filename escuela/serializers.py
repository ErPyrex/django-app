from rest_framework import serializers
from .models import Docente, Asignatura, Estudiante, Inscripcion

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    asignaturas = AsignaturaSerializer(many=True, read_only=True)

    class Meta:
        model = Estudiante
        fields = ('id', 'nombre', 'asignaturas')

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'
