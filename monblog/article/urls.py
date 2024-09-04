from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil),
    path('liste/', views.liste_article, name='liste'),
    path('<int:id>/', views.detail_article, name="detail"),
    path('contact/', views.contact, name='contact'),
]
