from django.test import TestCase
from .models import Consultation
from bibliothecaire.models import Media, Emprunteur
from datetime import date

class ConsultationModelTests(TestCase):
    fixtures = ['second_data.json', 'initial_data.json']

    def test_creation_consultation(self):
        # Créer les objets nécessaires pour la consultation
        emprunteur = Emprunteur.objects.get(pk=1)
        media = Media.objects.get(pk=1)

        # Créer l'instance de Consultation
        consultation = Consultation.objects.create(
            emprunteur=emprunteur,
            media_consulte=media,
            date_consultation=date(2024, 8, 27)
        )

        # Vérifier que la consultation a bien été créée avec les bonnes données
        self.assertEqual(consultation.emprunteur.name, "John Doe")
        self.assertEqual(consultation.media_consulte.name, "Python Basics")
        self.assertEqual(str(consultation.date_consultation), "2024-08-27")
        self.assertEqual(str(consultation), "John Doe a consulté Python Basics")


