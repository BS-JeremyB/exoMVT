from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil),
    path('liste/', views.liste_article, name='liste'),
    path('<int:id>/', views.detail_article, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('creer_article/', views.creation_article, name='creer_article'),
    path('creer_auteur/', views.creation_auteur, name='creer_auteur'),
]
