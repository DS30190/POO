from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirection_bibliothecaire, name='redirection_bibliothecaire'),
    path('index/', views.index, name='index'),
    path('emprunteurs/', views.liste_emprunteurs, name='liste_emprunteurs'),
    path('emprunteurs/creer/', views.creer_emprunteur, name='creer_emprunteur'),
    path('emprunteurs/<int:pk>/mettre-a-jour/', views.mettre_a_jour_emprunteur, name='mettre_a_jour_emprunteur'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('medias/ajouter/', views.ajouter_media, name='ajouter_media'),
    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('emprunts/creer/', views.creer_emprunt, name='creer_emprunt'),
    path('emprunts/<int:pk>/retourner/', views.retourner_emprunt, name='retourner_emprunt'),
]

