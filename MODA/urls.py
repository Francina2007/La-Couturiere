from django.urls import path
from . import views

urlpatterns = [
path('evaluacion2/', views.mostrar_reseñas, name='listado.html'),
]