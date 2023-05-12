from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html',context={
       'name':'Emir Neves'
    })

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse('sobre')

def my_ip(request):
    #ip_publico =  Request.get('https://api.ipify.org/')
    return HttpResponse('Mostrar Meu IP')