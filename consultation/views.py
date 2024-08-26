from django.shortcuts import render
from bibliothecaire.models import Media

def liste_medias_disponibles(request):
    medias = Media.objects.filter(disponible=True)
    return render(request, 'consultation/liste_medias_disponibles.html', {'medias': medias})

