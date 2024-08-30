from django.test import TestCase
from .models import Media, Emprunteur, Emprunt
from django.utils import timezone
from datetime import timedelta

class MediaModelTests(TestCase):
    fixtures = ['initial_data.json']  # Assure-toi que ce fichier est correct et contient des données valides

    def test_creation_livre(self):
        # Crée un objet Media de type "Livre" et vérifie ses attributs
        livre = Media.objects.create(type_media="Livre", name="1984")
        self.assertEqual(livre.name, "1984")
        self.assertEqual(livre.type_media, "Livre")
        self.assertTrue(livre.disponible)  # Vérifie que le média est disponible par défaut

    def test_creation_dvd(self):
        # Crée un objet Media de type "DVD" et vérifie ses attributs
        dvd = Media.objects.create(type_media="DVD", name="Inception")
        self.assertEqual(dvd.name, "Inception")
        self.assertEqual(dvd.type_media, "DVD")
        self.assertTrue(dvd.disponible)  # Vérifie que le média est disponible par défaut

class EmprunteurModelTests(TestCase):
    fixtures = ['initial_data.json']  # Assure-toi que ce fichier est correct et contient des données valides

    def test_creation_emprunteur(self):
        # Crée un objet Emprunteur et vérifie ses attributs
        emprunteur = Emprunteur.objects.create(name="Jane Doe")
        self.assertEqual(emprunteur.name, "Jane Doe")
        self.assertFalse(emprunteur.bloque)  # Vérifie que l'emprunteur n'est pas bloqué par défaut

    def test_emprunt_media(self):
        # Crée un objet Emprunteur et un objet Media, puis ajoute le Media aux emprunts de l'Emprunteur
        emprunteur = Emprunteur.objects.create(name="Jane Doe")
        livre = Media.objects.create(type_media="Livre", name="1984")
        emprunteur.emprunts.add(livre)
        # Vérifie que l'emprunteur a bien emprunté le livre
        self.assertIn(livre, emprunteur.emprunts.all())

class EmpruntModelTests(TestCase):
    fixtures = ['initial_data.json']  # Assure-toi que ce fichier est correct et contient des données valides

    def setUp(self):
        # Initialise les données nécessaires pour les tests
        self.media = Media.objects.create(type_media="Livre", name="1984")
        self.emprunteur = Emprunteur.objects.create(name="Jane Doe")

    def test_creation_emprunt(self):
        # Crée un objet Emprunt et vérifie ses attributs
        emprunt = Emprunt.objects.create(media=self.media, emprunteur=self.emprunteur, date_emprunt=timezone.now())
        self.assertEqual(emprunt.media, self.media)
        self.assertEqual(emprunt.emprunteur, self.emprunteur)
        self.assertIsNotNone(emprunt.date_emprunt)

    def test_retour_emprunt(self):
        # Crée un objet Emprunt, le marque comme retourné, et vérifie que le média est disponible
        emprunt = Emprunt.objects.create(media=self.media, emprunteur=self.emprunteur, date_emprunt=timezone.now())
        emprunt.date_retour = timezone.now() + timedelta(days=1)
        emprunt.save()
        self.assertTrue(emprunt.media.disponible)  # Vérifie que le média est disponible après le retour







