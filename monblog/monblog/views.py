from django.http import HttpResponse

def accueil(request):
    return HttpResponse('Bonjour, bienvenue sur MonBlog !')