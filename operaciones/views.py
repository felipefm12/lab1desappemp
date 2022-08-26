from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def suma(request, n1, n2):
    return HttpResponse( str(n1) + "+"+ str(n2) +"="+ str(n1+n2) )

def resta(request, n1, n2):
    return HttpResponse( str(n1) + "-" + str(n2) +"="+ str(n1-n2))

def multiplicacion(request, n1, n2):
    return HttpResponse( str(n1) + "*" + str(n2) +"="+ str(n1*n2))