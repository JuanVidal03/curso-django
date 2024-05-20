from django.shortcuts import render
from django.http import HttpResponse

# funcion que retorna un mensaje de prueba
def hello(request):
    return HttpResponse("Hello world")