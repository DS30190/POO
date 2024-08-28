from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('medias-disponibles/', views.liste_medias_disponibles, name='liste_medias_disponibles'),
]


