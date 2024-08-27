from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirection_consultation, name='redirection_consultation'),
    path('index/', views.index, name='index'),
    path('medias-disponibles/', views.liste_medias_disponibles, name='liste_medias_disponibles'),
]

