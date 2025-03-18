# Importation des modules nécessaires de Django
from django import forms  # Importation du module forms de Django pour créer des formulaires
from django.contrib.auth.models import User  # Importation du modèle User pour gérer les utilisateurs
from django.contrib.auth.forms import UserCreationForm  # Importation du formulaire UserCreationForm pour la création d'utilisateurs
from .models import Recette  # Importation du modèle Recette depuis les modèles de l'application
from .models import Commentaire  # Importation du modèle Commentaire depuis les modèles de l'application

# Formulaire d'inscription
class InscriptionForm(UserCreationForm):  # Définition d'une classe de formulaire pour l'inscription des utilisateurs, héritant de UserCreationForm
    # Champ email avec des messages d'erreur personnalisés
    email = forms.EmailField(required=True, error_messages={
        'required': 'L\'adresse email est obligatoire.',  # Message d'erreur si le champ email est requis mais non fourni
        'invalid': 'L\'adresse email n\'est pas valide.',  # Message d'erreur si l'adresse email fournie n'est pas valide
    })
    
    class Meta:  # Classe interne Meta pour définir des métadonnées pour le formulaire
        model = User  # Le modèle associé à ce formulaire est le modèle User
        fields = ["username", "email", "password1", "password2"]  # Champs du formulaire à inclure
        error_messages = {  # Messages d'erreur personnalisés pour les champs du formulaire
            'username': {
                'required': 'Le nom d\'utilisateur est obligatoire.',  # Message d'erreur si le champ username est requis mais non fourni
                'max_length': 'Le nom d\'utilisateur ne peut pas dépasser 150 caractères.',  # Message d'erreur si le nom d'utilisateur dépasse 150 caractères
                'invalid': 'Entrez un nom d\'utilisateur valide. Cette valeur peut contenir uniquement des lettres, des chiffres et les caractères @/./+/-/_ .',  # Message d'erreur si le nom d'utilisateur contient des caractères invalides
            },
            'password1': {
                'required': 'Le mot de passe est obligatoire.',  # Message d'erreur si le champ password1 est requis mais non fourni
                'min_length': 'Le mot de passe doit contenir au moins 8 caractères.',  # Message d'erreur si le mot de passe contient moins de 8 caractères
            },
            'password2': {
                'required': 'La confirmation du mot de passe est obligatoire.',  # Message d'erreur si le champ password2 est requis mais non fourni
                'match': 'Les mots de passe ne correspondent pas.',  # Message d'erreur si les mots de passe ne correspondent pas
            }
        }

# Formulaire de connexion
class ConnexionForm(forms.Form):  # Définition d'une classe de formulaire pour la connexion des utilisateurs
    # Champ nom d'utilisateur avec un message d'erreur personnalisé
    username = forms.CharField(
        error_messages={
            'required': 'Le nom d\'utilisateur est obligatoire.',  # Message d'erreur si le champ username est requis mais non fourni
        }
    )
    # Champ mot de passe avec un widget PasswordInput et un message d'erreur personnalisé
    password = forms.CharField(
        widget=forms.PasswordInput,  # Utilisation du widget PasswordInput pour masquer le mot de passe lors de la saisie
        error_messages={
            'required': 'Le mot de passe est obligatoire.',  # Message d'erreur si le champ password est requis mais non fourni
        }
    )

# Formulaire de recette
class RecetteForm(forms.ModelForm):  # Définition d'une classe de formulaire pour la création et la modification de recettes, héritant de ModelForm
    class Meta:  # Classe interne Meta pour définir des métadonnées pour le formulaire
        model = Recette  # Le modèle associé à ce formulaire est le modèle Recette
        fields = ['titre', 'description', 'ingredients', 'image']  # Champs du formulaire à inclure
    
    # Champ titre avec des attributs de widget personnalisés
    titre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la recette'}))  # Champ titre avec une longueur maximale de 255 caractères et des attributs de widget personnalisés
    # Champ description avec des attributs de widget personnalisés
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description de la recette'}))  # Champ description avec des attributs de widget personnalisés
    # Champ ingrédients avec des attributs de widget personnalisés
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Liste des ingrédients'}))  # Champ ingrédients avec des attributs de widget personnalisés
    # Champ image avec des attributs de widget personnalisés, non requis
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))  # Champ image avec des attributs de widget personnalisés, non requis

# Formulaire de commentaires
class CommentaireForm(forms.ModelForm):  # Définition d'une classe de formulaire pour la création et la modification de commentaires, héritant de ModelForm
    class Meta:  # Classe interne Meta pour définir des métadonnées pour le formulaire
        model = Commentaire  # Le modèle associé à ce formulaire est le modèle Commentaire
        fields = ['contenu']  # Champs du formulaire à inclure
    
    # Champ contenu avec des attributs de widget personnalisés
    contenu = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre commentaire'}))  # Champ contenu avec des attributs de widget personnalisés