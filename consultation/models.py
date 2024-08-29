from django.db import models

class Media(models.Model):
    # Vos champs ici
    titre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    # Autres champs selon vos besoins

    def __str__(self):
        return self.titre

class Consultation(models.Model):
    emprunteur = models.ForeignKey('bibliothecaire.Emprunteur', on_delete=models.CASCADE)
    media_consulte = models.ForeignKey('bibliothecaire.Media', on_delete=models.CASCADE)
    date_consultation = models.DateField()
