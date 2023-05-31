from django.shortcuts import render
from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })


# def my_ip(request):
    # ip_publico =  Request.get('https://api.ipify.org/')
#    return HttpResponse('Mostrar Meu IP')
