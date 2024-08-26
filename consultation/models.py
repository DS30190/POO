from django.db import models

class Consultation(models.Model):
    emprunteur = models.ForeignKey('bibliothecaire.Emprunteur', on_delete=models.CASCADE)
    media_consulte = models.ForeignKey('bibliothecaire.Media', on_delete=models.CASCADE)
    date_consultation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.emprunteur.name} a consulté {self.media_consulte.name}"

