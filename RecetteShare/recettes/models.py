from django.db import models
from django.contrib.auth.models import User

#créer les models

#model Recette
class Recette(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recettes/', blank=True, null=True) 
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

#model Commentaire
class Commentaire(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.utilisateur.username} sur {self.recette.titre}"