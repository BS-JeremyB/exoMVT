from django.forms import ModelForm
from django import forms
from .models import *

class Creation_Auteur_Form(ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'
    
    def clean_nom(self):

        nom = self.cleaned_data['nom']
        if 'batman' in nom.lower():
            raise forms.ValidationError("Le nom doit être correct !")
        return nom

class Creation_Article_Form(ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu','date_publication', 'auteur']
        widgets = {
            'date_publication': forms.DateInput(format="%d-%m-%Y", attrs={"type": "date"})
        }
