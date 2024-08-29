from django.shortcuts import render, redirect
from .models import Media

def index(request):
    return render(request, 'consultation/index.html')

def redirection_consultation(request):
    return redirect('index', permanent=True)  # Redirige vers 'consultation/index/'

def liste_medias_disponibles(request):
    medias = Media.objects.filter(disponible=True)
    return render(request, 'consultation/liste_medias_disponibles.html', {'medias': medias})

