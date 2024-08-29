from django.db import models

class Media(models.Model):
    # Vos champs ici
    titre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    # Autres champs selon vos besoins

    def __str__(self):
        return self.titre


