from django.shortcuts import render
from django.http import HttpResponse

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



