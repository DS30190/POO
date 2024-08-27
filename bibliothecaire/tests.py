from django.test import TestCase
from .models import Media, Emprunteur

class MediaModelTests(TestCase):
    fixtures = ['initial_data.json']  # Spécifie le fichier de fixture à utiliser

    def test_creation_livre(self):
        livre = Media.objects.create(type_media="Livre", name="1984")
        self.assertEqual(livre.name, "1984")
        self.assertEqual(livre.type_media, "Livre")
        self.assertTrue(livre.disponible)  # Vérifie que le média est disponible par défaut

    def test_creation_dvd(self):
        dvd = Media.objects.create(type_media="DVD", name="Inception")
        self.assertEqual(dvd.name, "Inception")
        self.assertEqual(dvd.type_media, "DVD")
        self.assertTrue(dvd.disponible)

class EmprunteurModelTests(TestCase):
    fixtures = ['initial_data.json']  # Spécifie le fichier de fixture à utiliser

    def test_creation_emprunteur(self):
        emprunteur = Emprunteur.objects.create(name="John Doe")
        self.assertEqual(emprunteur.name, "John Doe")
        self.assertFalse(emprunteur.bloque)  # Vérifie que l'emprunteur n'est pas bloqué par défaut

    def test_emprunt_media(self):
        emprunteur = Emprunteur.objects.create(name="Jane Doe")
        livre = Media.objects.create(type_media="Livre", name="1984")
        emprunteur.emprunts.add(livre)

        # Vérifie que l'emprunteur a bien emprunté le livre
        self.assertIn(livre, emprunteur.emprunts.all())





