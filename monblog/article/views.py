from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.


def accueil(request):
    return HttpResponse('Bonjour, bienvenue sur MonBlog !')


def liste_article(request):
    articles = Article.objects.all()
    articles_titres = Article.objects.values('titre', 'contenu')

    return render(request, 'liste.html', {'articles':articles, 'articles_titres':articles_titres})

def contact(request):
    return render(request, 'contact.html')


def detail_article(request, pk):
    article = Article.objects.get(id=pk)

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

def supprimer_article(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('liste')

def modifier_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == 'POST':
        form = Creation_Article_Form(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('liste')
        
    form = Creation_Article_Form(instance=article)
    return render(request, 'modifier.html', {'form':form})
                