from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Emir Neves',
    })


# def my_ip(request):
    # ip_publico =  Request.get('https://api.ipify.org/')
#    return HttpResponse('Mostrar Meu IP')
