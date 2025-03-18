from django.urls import path
from .views import inscription, connexion, deconnexion
from . import views  #
urlpatterns = [
     path('', views.accueil, name='accueil'),
    path("inscription/", inscription, name="inscription"),
    path("connexion/", connexion, name="connexion"),
    path("deconnexion/", deconnexion, name="deconnexion"),
    # Afficher les recettes de l'utilisateur connecté
    path('mes_recettes/', views.mes_recettes, name='mes_recettes'),

    # Ajouter une recette
    path('create_recette/', views.create_recette, name='create_recette'),


    # Modifier une recette
    path('modifier_recette/<int:recette_id>/', views.modifier_recette, name='modifier_recette'),

    # Supprimer une recette
    path('supprimer_recette/<int:recette_id>/', views.supprimer_recette, name='supprimer_recette'),

    # Voir les détails d'une recette
    path('recette/<int:recette_id>/', views.detail_recette, name='detail_recette'),
]
