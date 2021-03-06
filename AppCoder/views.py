from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario
from django.http import HttpResponse

# Create your views here.

def curso(request):
      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

      return HttpResponse(documentoDeTexto)


def inicio(request):
      return render(request, "AppCoder/inicio.html")

def cursos(request):
      return render(request, "AppCoder/cursos.html")

def profesores(request):
      return render(request, "AppCoder/profesores.html")


def estudiantes(request):
      return render(request, "AppCoder/estudiantes.html")


def entregables(request):
      return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = CursoFormulario()
      return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
      return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
      respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"

      return HttpResponse(respuesta)