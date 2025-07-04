from django.contrib import admin
from .models import Docente, Asignatura, Estudiante, Inscripcion

class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines = (InscripcionInline,)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'docente')
    list_filter = ('docente',)

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'asignatura', 'fecha_inscripcion')
    list_filter = ('asignatura__docente', 'asignatura')
