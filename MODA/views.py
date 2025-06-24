from django.shortcuts import render
from .models import Lacouturière

def mostrar_reseñas(request):
    reseñas = Lacouturière.objects.all()
    return render(request, 'moda/listado.html', {'reseñas': reseñas})
