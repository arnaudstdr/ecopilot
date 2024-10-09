from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Revenu, DepenseRecurrente, DepensePonctuelle
from .forms import RevenuForm, DepesneRecurrentForm, DepensePonctuelleForm, UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from datetime import date, datetime
import calendar
import locale

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'finances/home.html')

@login_required
def dashboard(request, year=None, month=None):
    # Si le mois et l'année ne sont pas précisés, utilise le mois courant
    if not year or not month:
        today = date.today()
        year = today.year
        month = today.month

    # Obtenir le premier et le dernier jour du mois
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month, calendar.monthrange(year, month)[1])

    # Filtrer les données en fonction du mois sélectionné
    revenus = Revenu.objects.filter(utilisateur=request.user, date_reception__range=[first_day, last_day])
    depenses_recurrentes = DepenseRecurrente.objects.filter(utilisateur=request.user, date_debut__lte=last_day)
    depenses_ponctuelles = DepensePonctuelle.objects.filter(utilisateur=request.user, date__range=[first_day, last_day])

    total_revenu = sum(revenu.montant for revenu in revenus)
    total_depenses_recurrentes = sum(depense.montant for depense in depenses_recurrentes if depense.statut)
    total_depenses_ponctuelles = sum(depense.montant for depense in depenses_ponctuelles)

    solde = total_revenu - (total_depenses_recurrentes + total_depenses_ponctuelles)
    
    # Calcule des mois précédents et suivants pour la navigation
    prev_month = (month - 1) if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = (month + 1) if month < 12 else 1
    next_year = year if month < 12 else year + 1

    # Configurer le locale en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    # Obtenir le nom du mois
    month_name = first_day.strftime('%B')

    # On transmet les données nécessaires pour les graphiques
    context = {
        'revenus': revenus,
        'depenses_recurrentes': depenses_recurrentes,
        'depenses_ponctuelles': depenses_ponctuelles,
        'total_revenu': total_revenu,
        'total_depenses_recurrentes': total_depenses_recurrentes,
        'total_depenses_ponctuelles': total_depenses_ponctuelles,
        'solde': solde,
        'year': year,
        'month': month,
        'month_name': month_name,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year
    }
    return render(request, 'finances/dashboard.html', context)

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