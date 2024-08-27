from django.shortcuts import render, redirect
from bibliothecaire.models import Media

def liste_medias_disponibles(request):
    # Assurez-vous que cette vue est correctement utilisée dans les URLs
    medias = Media.objects.filter(disponible=True)
    return render(request, 'consultation/liste_medias_disponibles.html', {'medias': medias})

def index(request):
    return render(request, 'consultation/index.html')

def redirection_consultation(request):
    # Redirige vers la vue 'index'
    return redirect('index', permanent=True)
