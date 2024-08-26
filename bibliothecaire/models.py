from django.db import models

class Media(models.Model):
    MEDIA_CHOICES = (
        ('Livre', 'Livre'),
        ('DVD', 'DVD'),
        ('CD', 'CD'),
        ('Jeu de Plateau', 'Jeu de Plateau'),
    )
    type_media = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    name = models.CharField(max_length=255)
    date_emprunt = models.DateField(blank=True, null=True)
    disponible = models.BooleanField(default=True)

class Emprunteur(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)
    emprunts = models.ManyToManyField(Media, through='Emprunt')

class Emprunt(models.Model):
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField(null=True, blank=True)


