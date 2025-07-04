from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente, Asignatura, Estudiante, Inscripcion
from .serializers import DocenteSerializer, AsignaturaSerializer, EstudianteSerializer, InscripcionSerializer

# API ViewSets
class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    @action(detail=True, methods=['post'])
    def inscribir(self, request, pk=None):
        estudiante = self.get_object()
        asignatura_id = request.data.get('asignatura_id')
        if not asignatura_id:
            return Response({'error': 'Falta asignatura_id'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            asignatura = Asignatura.objects.get(id=asignatura_id)
            Inscripcion.objects.create(estudiante=estudiante, asignatura=asignatura)
            return Response({'status': 'inscripción creada'}, status=status.HTTP_201_CREATED)
        except Asignatura.DoesNotExist:
            return Response({'error': 'Asignatura no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

# Vistas de Plantillas HTML
def app_index(request):
    return render(request, 'escuela/index.html')

def docente_list(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            Docente.objects.create(nombre=nombre)
        return redirect('docente_list')
    docentes = Docente.objects.all()
    return render(request, 'escuela/docente_list.html', {'docentes': docentes})

def docente_detail(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        asignatura_id = request.POST.get('asignatura')
        if asignatura_id:
            asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
            docente.asignaturas.add(asignatura)
    
    todas_las_asignaturas = Asignatura.objects.all()
    return render(request, 'escuela/docente_detail.html', {
        'docente': docente,
        'todas_las_asignaturas': todas_las_asignaturas
    })

def asignatura_list(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        docente_id = request.POST.get('docente')
        if nombre and docente_id:
            docente = get_object_or_404(Docente, pk=docente_id)
            Asignatura.objects.create(nombre=nombre, docente=docente)
        return redirect('asignatura_list')
    
    asignaturas = Asignatura.objects.all()
    docentes = Docente.objects.all()
    return render(request, 'escuela/asignatura_list.html', {'asignaturas': asignaturas, 'docentes': docentes})

def estudiante_list(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            Estudiante.objects.create(nombre=nombre)
        return redirect('estudiante_list')
    estudiantes = Estudiante.objects.all()
    return render(request, 'escuela/estudiante_list.html', {'estudiantes': estudiantes})

def estudiante_detail(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        asignatura_id = request.POST.get('asignatura')
        if asignatura_id:
            asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
            Inscripcion.objects.get_or_create(estudiante=estudiante, asignatura=asignatura)
    
    asignaturas_inscritas = estudiante.asignaturas.all()
    todas_las_asignaturas = Asignatura.objects.exclude(id__in=asignaturas_inscritas.values_list('id', flat=True))
    
    return render(request, 'escuela/estudiante_detail.html', {
        'estudiante': estudiante,
        'asignaturas_inscritas': asignaturas_inscritas,
        'todas_las_asignaturas': todas_las_asignaturas
    })
