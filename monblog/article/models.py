from django.db import models

# Create your models here.

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.prenom} {self.nom}'


class Article(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication = models.DateField()
    auteur = models.ManyToManyField(Auteur)

    class Meta:
        permissions = [
            ('Peut_Modifier_Article','peut modifier un article')
        ]
    def __str__(self):
        return f'{self.titre}'
    
    