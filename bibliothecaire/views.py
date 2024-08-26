from django.shortcuts import render, get_object_or_404, redirect
from .models import Emprunteur, Media, Emprunt
from .forms import EmprunteurForm, MediaForm, EmpruntForm

# Liste des membres
def liste_emprunteurs(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/liste_emprunteurs.html', {'emprunteurs': emprunteurs})

# Créer un membre
def creer_emprunteur(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_emprunteurs')
    else:
        form = EmprunteurForm()
    return render(request, 'bibliothecaire/creer_emprunteur.html', {'form': form})

# Mettre à jour un membre
def mettre_a_jour_emprunteur(request, pk):
    emprunteur = get_object_or_404(Emprunteur, pk=pk)
    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=emprunteur)
        if form.is_valid():
            form.save()
            return redirect('liste_emprunteurs')
    else:
        form = EmprunteurForm(instance=emprunteur)
    return render(request, 'bibliothecaire/creer_emprunteur.html', {'form': form})

# Liste des médias
def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/liste_medias.html', {'medias': medias})

# Ajouter un média
def ajouter_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')
    else:
        form = MediaForm()
    return render(request, 'bibliothecaire/ajouter_media.html', {'form': form})

# Créer un emprunt
def creer_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)
            media = emprunt.media
            if media.disponible:
                media.disponible = False
                media.save()
                emprunt.save()
                return redirect('liste_emprunts')
            else:
                form.add_error(None, 'Le média n\'est pas disponible.')
    else:
        form = EmpruntForm()
    return render(request, 'bibliothecaire/creer_emprunt.html', {'form': form})

# Retourner un emprunt
def retourner_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    media = emprunt.media
    media.disponible = True
    media.save()
    emprunt.date_retour = date.today()
    emprunt.save()
    return redirect('liste_emprunts')

# Liste des emprunts
def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'bibliothecaire/liste_emprunts.html', {'emprunts': emprunts})

