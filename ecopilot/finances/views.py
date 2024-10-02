from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Revenu, DepenseRecurrente, DepensePonctuelle
from .forms import RevenuForm, DepesneRecurrentForm, DepensePonctuelleForm, UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from datetime import date

# Create your views here.
@login_required
def dashboard(request):
    revenus = Revenu.objects.filter(utilisateur=request.user, date_reception__month=date.today().month)
    depenses_recurrentes = DepenseRecurrente.objects.filter(utilisateur=request.user)
    depenses_ponctuelles = DepensePonctuelle.objects.filter(utilisateur=request.user, date__month=date.today().month)

    total_revenu = sum(revenu.montant for revenu in revenus)
    total_depenses_recurrentes = sum(depense.montant for depense in depenses_recurrentes if depense.statut)
    total_depenses_ponctuelles = sum(depense.montant for depense in depenses_ponctuelles)

    solde = total_revenu - (total_depenses_recurrentes + total_depenses_ponctuelles)
    
    # On transmet les données nécessaires pour les graphiques
    context = {
        'total_revenu': total_revenu,
        'total_depenses_recurrentes': total_depenses_recurrentes,
        'total_depenses_ponctuelles': total_depenses_ponctuelles,
        'solde': solde
    }
    return render(request, 'finances/dashboard.html', {
        'revenus': revenus,
        'depenses_recurrentes': depenses_recurrentes,
        'depenses_ponctuelles': depenses_ponctuelles,
        'total_revenu': total_revenu,
        'total_depenses_recurrentes': total_depenses_recurrentes,
        'total_depenses_ponctuelles': total_depenses_ponctuelles,
        'solde': solde
    })

@login_required
def ajout_revenu(request):
    if request.method == 'POST':
        form = RevenuForm(request.POST)
        if form.is_valid():
            revenu = form.save(commit=False)
            revenu.utilisateur = request.user
            revenu.save()
            return redirect('dashboard')
    else:
        form = RevenuForm()

    return render(request, 'finances/ajout_revenu.html', {'form': form})

@login_required
def ajout_depense_recurrente(request):
    if request.method == 'POST':
        form = DepesneRecurrentForm(request.POST)
        if form.is_valid():
            depense_recurrente = form.save(commit=False)
            depense_recurrente.utilisateur = request.user
            depense_recurrente.save()
            return redirect('dashboard')  # Redirection vers le tableau de bord après l'ajout
    else:
        form = DepesneRecurrentForm()

    return render(request, 'finances/ajout_depense_recurrente.html', {'form': form})

@login_required
def ajout_depense_ponctuelle(request):
    if request.method == 'POST':
        form = DepensePonctuelleForm(request.POST)
        if form.is_valid():
            depense_ponctuelle = form.save(commit=False)
            depense_ponctuelle.utilisateur = request.user
            depense_ponctuelle.save()
            return redirect('dashboard')  # Redirection vers le tableau de bord après l'ajout
    else:
        form = DepensePonctuelleForm()

    return render(request, 'finances/ajout_depense_ponctuelle.html', {'form': form})

@login_required
def pointer_depense_recurrente(request, pk):
    depense = get_object_or_404(DepenseRecurrente, pk=pk, utilisateur=request.user)
    depense.statut = not depense.statut
    depense.save()
    return redirect('dashboard')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})