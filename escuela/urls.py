from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DocenteViewSet, AsignaturaViewSet, EstudianteViewSet, InscripcionViewSet,
    app_index, docente_list, docente_detail, asignatura_list, estudiante_list, estudiante_detail
)

# Configuración de la API
router = DefaultRouter()
router.register(r'docentes', DocenteViewSet)
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'inscripciones', InscripcionViewSet)

# URLs de la Interfaz de Usuario
urlpatterns = [
    # Rutas de la interfaz de usuario
    path('', app_index, name='app_index'),
    path('docentes/', docente_list, name='docente_list'),
    path('docentes/<int:pk>/', docente_detail, name='docente_detail'),
    path('asignaturas/', asignatura_list, name='asignatura_list'),
    path('estudiantes/', estudiante_list, name='estudiante_list'),
    path('estudiantes/<int:pk>/', estudiante_detail, name='estudiante_detail'),

    # Ruta de la API
    path('api/', include(router.urls)),
]
