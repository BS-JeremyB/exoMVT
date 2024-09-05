from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.


def accueil(request):
    return HttpResponse('Bonjour, bienvenue sur MonBlog !')


def liste_article(request):
    articles = [{'id':1,'titre':'article 1', 'auteur': 'John Doe', 'contenu':'lorem ipsum'},{'id':2,'titre':'article 2', 'auteur': 'Jane Doe', 'contenu':'lorem ipsum bis'}]

    return render(request, 'liste.html', {'articles':articles})

def contact(request):
    return render(request, 'contact.html')


def detail_article(request, id):
    articles = [{'id':1,'titre':'article 1', 'auteur': 'John Doe', 'contenu':'lorem ipsum'},{'id':2,'titre':'article 2', 'auteur': 'Jane Doe', 'contenu':'lorem ipsum bis'}]
    
    article = next(article for article in articles if article['id'] == id)

    return render(request, 'detail.html', {'article': article} )


def creation_article(request):
    if request.method == "POST":
        form = Creation_Article_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("liste")
        
    return render(request, 'formulaire_creation.html', {'form': Creation_Article_Form, 'titre': 'Création Article'})

def creation_auteur(request):
    if request.method == "POST":
        form = Creation_Auteur_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("liste")

    else:  
        form = Creation_Auteur_Form()
        
    return render(request, 'formulaire_creation.html', {'form': form, 'titre': 'Création Auteur'})