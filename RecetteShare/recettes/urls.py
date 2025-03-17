from django.urls import path
from .views import inscription, connexion, deconnexion
from . import views  #
urlpatterns = [
     path('', views.accueil, name='accueil'),
    path("inscription/", inscription, name="inscription"),
    path("connexion/", connexion, name="connexion"),
    path("deconnexion/", deconnexion, name="deconnexion"),
]
