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

    # Ajouter un commentaire à une recette
    path('recette/<int:recette_id>/ajouter_commentaire/', views.ajouter_commentaire, name='ajouter_commentaire'),
    # Afficher les commentaires d'une recette
    path('recette/<int:recette_id>/commentaires/', views.recette_commentaires, name='commentaires'),
    # Supprimer un commentaire
    path('recette/<int:recette_id>/commentaire/<int:commentaire_id>/supprimer/', views.supprimer_commentaire, name='supprimer_commentaire'),
]
