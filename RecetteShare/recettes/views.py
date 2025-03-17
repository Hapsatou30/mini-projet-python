from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import InscriptionForm, ConnexionForm
from django.contrib import messages

# Inscription
def inscription(request):
    if request.method == "POST":
        # Si la méthode est POST, on crée une instance du formulaire avec les données soumises
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide, on enregistre le nouvel utilisateur
            form.save()
            # On affiche un message de succès
            messages.success(request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
            # On redirige l'utilisateur vers la page de connexion
            return redirect("connexion")
        else:
            # Si le formulaire est invalide, les erreurs seront affichées
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        # Si la méthode n'est pas POST, on crée une instance vide du formulaire
        form = InscriptionForm()
    # On rend la page d'inscription avec le formulaire
    return render(request, "recettes/inscription.html", {"form": form})

# Connexion
def connexion(request):
    if request.method == "POST":
        # Si la méthode est POST, on crée une instance du formulaire avec les données soumises
        form = ConnexionForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide, on récupère les données nettoyées
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # On authentifie l'utilisateur
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Si l'utilisateur est authentifié, on le connecte
                login(request, user)
                # On affiche un message de succès
                messages.success(request, "Connexion réussie !")
                # On redirige l'utilisateur vers la page d'accueil
                return redirect("accueil")
            else:
                # Si l'authentification échoue, on affiche un message d'erreur
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            # Si le formulaire est invalide, on affiche les erreurs
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        # Si la méthode n'est pas POST, on crée une instance vide du formulaire
        form = ConnexionForm()
    # On rend la page de connexion avec le formulaire
    return render(request, "recettes/connexion.html", {"form": form})

# Déconnexion
def deconnexion(request):
    # On déconnecte l'utilisateur
    logout(request)
    # On affiche un message de succès
    messages.success(request, "Vous avez été déconnecté.")
    # On redirige l'utilisateur vers la page de connexion
    return redirect("connexion")

# Page d'accueil
def accueil(request):
    # On rend la page d'accueil
    return render(request, "recettes/accueil.html")