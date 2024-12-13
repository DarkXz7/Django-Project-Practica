from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request): #esto es la funcion que luego debo llamar en las url
    return HttpResponse("Hola mundo")

def about(request):
    return HttpResponse("About ")