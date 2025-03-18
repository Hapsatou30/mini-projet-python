from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import InscriptionForm, ConnexionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Recette
from .forms import RecetteForm
from django.core.paginator import Paginator
from .forms import CommentaireForm
from.models import Commentaire



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
def accueil(request):  # Définition de la fonction accueil qui prend en paramètre la requête HTTP
    recettes = Recette.objects.all()  # Récupère toutes les recettes de la base de données
    paginator = Paginator(recettes, 6)  # 6 recettes par page
    page_number = request.GET.get('page')  # Récupère le numéro de page depuis l'URL
    recettes = paginator.get_page(page_number)  # Récupère les recettes de la page demandée
    return render(request, 'recettes/accueil.html', {'recettes': recettes})  # La fonction render génère une réponse HTTP avec le contenu du template "recettes/accueil.html" et passe toutes les recettes au contexte

# Afficher les recettes de l'utilisateur connecté
@login_required  # Décorateur qui restreint l'accès à cette vue aux utilisateurs authentifiés
def mes_recettes(request):  # Définition de la fonction mes_recettes qui prend en paramètre la requête HTTP
    # Récupère les recettes de l'utilisateur connecté
    recettes = Recette.objects.filter(auteur=request.user)  # Filtre les recettes pour ne récupérer que celles dont l'auteur est l'utilisateur connecté
    # Rend la page mes_recettes.html avec les recettes de l'utilisateur
    return render(request, 'recettes/mes_recettes.html', {'recettes': recettes})  # La fonction render génère une réponse HTTP avec le contenu du template "recettes/mes_recettes.html" et passe les recettes de l'utilisateur au contexte


# Ajouter une recette
@login_required  # Décorateur qui restreint l'accès à cette vue aux utilisateurs authentifiés
def create_recette(request):  # Définition de la fonction create_recette qui prend en paramètre la requête HTTP
    if request.method == 'POST':  # Vérifie si la méthode de la requête est POST
        # Si la méthode est POST, on crée une instance du formulaire avec les données soumises
        form = RecetteForm(request.POST, request.FILES)  # Crée une instance du formulaire RecetteForm avec les données POST et les fichiers téléchargés
        if form.is_valid():  # Vérifie si le formulaire est valide
            # Si le formulaire est valide, on enregistre la recette sans la sauvegarder immédiatement
            recette = form.save(commit=False)  # Enregistre la recette sans la sauvegarder immédiatement dans la base de données
            # Associe l'utilisateur connecté comme auteur de la recette
            recette.auteur = request.user  # Associe l'utilisateur connecté comme auteur de la recette
            # Sauvegarde la recette dans la base de données
            recette.save()  # Sauvegarde la recette dans la base de données
            # Redirige vers la page mes recettes après la création
            return redirect('mes_recettes')  # Redirige l'utilisateur vers la page mes_recettes après la création de la recette
    else:  # Si la méthode n'est pas POST
        # Si la méthode n'est pas POST, on crée une instance vide du formulaire
        form = RecetteForm()  # Crée une instance vide du formulaire RecetteForm
    
    # On rend la page de création de recette avec le formulaire
    return render(request, 'recettes/create_recette.html', {'form': form})  # La fonction render génère une réponse HTTP avec le contenu du template "recettes/create_recette.html" et passe le formulaire au contexte


#modifier une recette
@login_required
def modifier_recette(request, recette_id):  # Définition de la fonction modifier_recette qui prend en paramètre la requête HTTP et l'identifiant de la recette
    recette = get_object_or_404(Recette, id=recette_id)  # Récupère la recette avec l'identifiant donné ou renvoie une erreur 404 si elle n'existe pas

    if request.method == 'POST':  # Vérifie si la méthode de la requête est POST
        form = RecetteForm(request.POST, request.FILES, instance=recette)  # Crée une instance du formulaire RecetteForm avec les données POST et les fichiers téléchargés, et associe la recette existante
        if form.is_valid():  # Vérifie si le formulaire est valide
            form.save()  # Sauvegarde les modifications de la recette dans la base de données
            return redirect('mes_recettes')  # Redirige vers la page mes recettes après modification
    else:  # Si la méthode n'est pas POST
        form = RecetteForm(instance=recette)  # Crée une instance du formulaire RecetteForm avec la recette existante pour pré-remplir le formulaire

    return render(request, 'recettes/modifier_recette.html', {'form': form})  # La fonction render génère une réponse HTTP avec le contenu du template "modifier_recette.html" et passe le formulaire au contexte

# Supprimer une recette
@login_required
def supprimer_recette(request, recette_id):  # Définition de la fonction supprimer_recette qui prend en paramètre la requête HTTP et l'identifiant de la recette
    recette = get_object_or_404(Recette, id=recette_id)  # Récupère la recette avec l'identifiant donné ou renvoie une erreur 404 si elle n'existe pas
    recette.delete()  # Supprime la recette
    return redirect('mes_recettes')  # Redirige vers la page mes recettes après suppression

# voir les détails d'une recette
def detail_recette(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    commentaires = recette.commentaires.all().order_by("-date_creation")  # Trie les commentaires du plus récent au plus ancien
    return render(request, "recettes/detail_recette.html", {"recette": recette, "commentaires": commentaires})

# Ajouter un commentaire
@login_required
def ajouter_commentaire(request, recette_id):  # Définition de la fonction ajouter_commentaire qui prend en paramètre la requête HTTP et l'identifiant de la recette
    recette = get_object_or_404(Recette, id=recette_id)  # Récupère la recette avec l'identifiant donné ou renvoie une erreur 404 si elle n'existe pas

    if request.method == 'POST':  # Vérifie si la méthode de la requête est POST
        form = CommentaireForm(request.POST)  # Crée une instance du formulaire CommentaireForm avec les données POST
        if form.is_valid():  # Vérifie si le formulaire est valide
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user  # Associe l'utilisateur connecté comme auteur du commentaire
            commentaire.recette = recette  # Associe la recette au commentaire
            commentaire.save()  # Sauvegarde le commentaire dans la base de données
            return redirect('detail_recette', recette_id=recette_id)  # Redirige vers la page de détail de la recette après la création du commentaire
    else:  # Si la méthode n'est pas POST
        form = CommentaireForm()  # Crée une instance vide du formulaire CommentaireForm
        return redirect('detail_recette', {'form': form, 'recette': recette})  # La fonction render génère une réponse HTTP avec le contenu du template "ajouter_commentaire.html" et passe le formulaire et la recette au contexte
    
# Supprimer un commentaire
@login_required
def supprimer_commentaire(request, recette_id, commentaire_id):  # Définition de la fonction supprimer_commentaire qui prend en paramètre la requête HTTP, l'identifiant de la recette et l'identifiant du commentaire
    commentaire = get_object_or_404(Commentaire, id=commentaire_id, recette_id=recette_id)  # Récupère le commentaire avec l'identifiant donné et l'identifiant de la recette ou renvoie une erreur 404 si elle n'existe pas
    commentaire.delete()  # Supprime le commentaire
    return redirect('detail_recette', recette_id=recette_id)

#afficher les commentaires par recette
def recette_commentaires(request, recette_id):  # Définition de la fonction recette_commentaires qui prend en paramètre la requête HTTP et l'identifiant de la recette
    recette = get_object_or_404(Recette, id=recette_id)  # Récupère la recette avec l'identifiant donné ou renvoie une erreur 404 si elle n'existe pas
    commentaires = recette.commentaires.all()  # Récupère tous les commentaires associés à la recette
    return render(request, 'recettes/détail_recette.html', {'recette': recette, 'commentaires': commentaires})