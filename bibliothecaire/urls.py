from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.redirection_bibliothecaire, name='redirection_bibliothecaire'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('emprunteurs/', views.liste_emprunteurs, name='liste_emprunteurs'),
    path('emprunteurs/creer/', views.creer_emprunteur, name='creer_emprunteur'),
    path('emprunteurs/<int:pk>/mettre-a-jour/', views.mettre_a_jour_emprunteur, name='mettre_a_jour_emprunteur'),
    path('medias/ajouter/', views.ajouter_media, name='ajouter_media'),
    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('emprunts/creer/', views.creer_emprunt, name='creer_emprunt'),
    path('emprunts/<int:pk>/retourner/', views.retourner_emprunt, name='retourner_emprunt'),
    path('ajoute_media/', views.ajouter_media, name='ajoute_media'),
    path('creer_emprunt/', views.creer_emprunt, name='creer_emprunt'),
    path('creer_emprunteur/', views.creer_emprunteur, name='creer_emprunteur'),
    path('liste_emprunteurs/', views.liste_emprunteurs, name='liste_emprunteurs'),
    path('liste_emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('liste_medias/', views.liste_medias, name='liste_medias'),
    path('emprunteurs/<int:pk>/mettre-a-jour/', views.mettre_a_jour_emprunteur, name='mettre_a_jour_emprunteur'),
    path('emprunt/<int:emprunt_id>/update/', views.update_emprunt, name='update_emprunt'),
]





