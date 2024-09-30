from django import forms
from .models import Revenu, DepenseRecurrente, DepensePonctuelle
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RevenuForm(forms.ModelForm):
    class Meta:
        model = Revenu
        fields = ['montant', 'source', 'date_reception']

class DepesneRecurrentForm(forms.ModelForm):
    class Meta:
        model = DepenseRecurrente
        fields = ['nom', 'montant', 'frequence', 'date_debut', 'date_fin']

class DepensePonctuelleForm(forms.ModelForm):
    class Meta:
        model = DepensePonctuelle
        fields = ['nom', 'montant', 'categorie', 'date']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']