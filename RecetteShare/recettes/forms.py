from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={
        'required': 'L\'adresse email est obligatoire.',
        'invalid': 'L\'adresse email n\'est pas valide.',
    })
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        error_messages = {
            'username': {
                'required': 'Le nom d\'utilisateur est obligatoire.',
                'max_length': 'Le nom d\'utilisateur ne peut pas dépasser 150 caractères.',
                 'invalid': 'Entrez un nom d\'utilisateur valide. Cette valeur peut contenir uniquement des lettres, des chiffres et les caractères @/./+/-/_ .',
          
            },
            'password1': {
                'required': 'Le mot de passe est obligatoire.',
                'min_length': 'Le mot de passe doit contenir au moins 8 caractères.',
            },
            'password2': {
                'required': 'La confirmation du mot de passe est obligatoire.',
                'match': 'Les mots de passe ne correspondent pas.',
            }
        }

# Formulaire de connexion
class ConnexionForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': 'Le nom d\'utilisateur est obligatoire.',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Le mot de passe est obligatoire.',
        }
    )