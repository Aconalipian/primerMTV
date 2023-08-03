from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime
from app1.models import *
from random import randint
from django.urls import path
from django.shortcuts import render



def bienvenida(request):
    nombre = "Arlette"
    apellido = "Cona Lipian"
       

    diccionario = {"nombre": nombre, "apellido": apellido}    
    plantilla = loader.get_template('mi_template.html')    
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)



def mostrar_familiares(request):
    Familia = Familiares.objects.all()
    return render(request, 'mostrar_familia.html', {'Familia': Familia})
