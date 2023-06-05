from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):


admin.site.register(Category, CategoryAdmin)    

# PARADO AQUI EM 05/06/2023
# REGISTREI O ERRO E FIZ A PERGUNTA NO GRUPO ( AULA 54) Minuto 9:25 / 13:56
# https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/learn/lecture/29515745#questions