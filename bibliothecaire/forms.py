# bibliothecaire/forms.py

from django import forms
from .models import Emprunteur, Media, Emprunt

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['name', 'bloque']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['type_media', 'name', 'disponible']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['emprunteur', 'media', 'date_retour']  # Ajout du champ date_retour
        widgets = {
            'date_retour': forms.DateInput(attrs={'type': 'date'}),
        }

