from django.shortcuts import render
from django.http import HttpResponse
from .models import libros


from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import viewsets

from .serializer import librosSerializer
# Create your views here.
def librosIndex(request):
    _libros= libros.objcts.all()
    return HttpResponse("<h1> BIENVENIDOS A HEMEROTECA <h1>")

class librosApiView(APIView):
    def get(self, request, *args, **kwargs):
        _libros = libros.objects.all()

        data_response = [{"titulo": libros.Título} for libros in _libros]

        return Response ({data_response})
    
    def post(self, request, *args, **kwargs):

        data = request.data

        _libro= libros(name=data.get("título"), fecha_de_publicación = data.get("fecha de publicación"),  editorial= data.get ("editorial"))
        _libro.save()

        return Response("message" : "Libro Agregado")

class librosViewSet(viewsets.ModelViewSet):
    serializer_class = librosSerializer
    queryset = libros.objects.all()
