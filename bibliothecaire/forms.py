from django import forms
from .models import Emprunteur, Media, Emprunt

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['name', 'bloque']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['type_media', 'name', 'date_emprunt', 'disponible']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['emprunteur', 'media']
