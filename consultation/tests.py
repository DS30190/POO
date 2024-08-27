from django.test import TestCase
from .models import Consultation
from bibliothecaire.models import Media, Emprunteur


class ConsultationModelTests(TestCase):
    fixtures = ['second_data.json']  # Charger les données initiales pour le test

    def test_creation_consultation(self):
        consultation = Consultation.objects.get(pk=1)

        # Vérifier que la consultation a bien été créée avec les bonnes données
        self.assertEqual(consultation.emprunteur.name, "John Doe")
        self.assertEqual(consultation.media_consulte.name, "Python Basics")
        self.assertEqual(str(consultation.date_consultation), "2024-08-27")
        self.assertEqual(str(consultation), "John Doe a consulté Python Basics")

