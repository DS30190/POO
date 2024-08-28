from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Media, Emprunteur, Emprunt
from .forms import EmprunteurForm, MediaForm, EmpruntForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'bibliothecaire/index.html')

def redirection_bibliothecaire(request):
    return redirect('index', permanent=True)


def liste_medias(request):
    livres = Media.objects.filter(type_media='Livre')
    dvds = Media.objects.filter(type_media='DVD')
    cds = Media.objects.filter(type_media='CD')
    jeux_de_plateau = Media.objects.filter(type_media='Jeu de Plateau')
    return render(request, 'bibliothecaire/liste_medias.html', {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux_de_plateau': jeux_de_plateau
    })


def liste_emprunteurs(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'bibliothecaire/liste_emprunteurs.html', {'emprunteurs': emprunteurs})


def creer_emprunteur(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emprunteur créé avec succès.')
            return redirect('liste_emprunteurs')
        else:
            messages.error(request, 'Formulaire invalide.')
    else:
        form = EmprunteurForm()
    return render(request, 'bibliothecaire/creer_emprunteur.html', {'form': form})


def mettre_a_jour_emprunteur(request, pk):
    emprunteur = get_object_or_404(Emprunteur, pk=pk)
    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=emprunteur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emprunteur mis à jour avec succès.')
            return redirect('liste_emprunteurs')
        else:
            messages.error(request, 'Formulaire invalide.')
    else:
        form = EmprunteurForm(instance=emprunteur)
    return render(request, 'bibliothecaire/mettre_a_jour_emprunteur.html', {'form': form})


def ajouter_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Média ajouté avec succès.')
            return redirect('liste_medias')
        else:
            messages.error(request, 'Formulaire invalide.')
    else:
        form = MediaForm()
    return render(request, 'bibliothecaire/ajouter_media.html', {'form': form})


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
                messages.success(request, 'Emprunt créé avec succès.')
                return redirect('liste_emprunts')
            else:
                form.add_error(None, 'Le média n\'est pas disponible.')
        else:
            messages.error(request, 'Formulaire invalide.')
    else:
        form = EmpruntForm()
    return render(request, 'bibliothecaire/creer_emprunt.html', {'form': form})


def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'bibliothecaire/liste_emprunts.html', {'emprunts': emprunts})


def retourner_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        emprunt.date_retour = date.today()
        emprunt.media.disponible = True
        emprunt.media.save()
        emprunt.save()
        messages.success(request, 'Emprunt retourné avec succès.')
        return redirect('liste_emprunts')
    return render(request, 'bibliothecaire/retourner_emprunt.html', {'emprunt': emprunt})


def liste_medias_disponibles(request):
    medias = Media.objects.filter(disponible=True)
    return render(request, 'consultation/liste_medias_disponibles.html', {'medias': medias})

@login_required
def liste_emprunteurs(request):
    # Logique ici
    pass