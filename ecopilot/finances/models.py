from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Revenu(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100)
    date_reception = models.DateField()

    def __str__(self):
        return f"{self.source} - {self.montant}€"
    
class DepenseRecurrente(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    frequence = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    statut = models.BooleanField(default=False)   # Pointé ou non

    def __str__(self):
        return f"{self.nom} - {self.montant}€ ({self.frequence})"
    
class DepensePonctuelle(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=50)   # Alimentation, Transport, etc.
    date = models.DateField()

    def __str__(self):
        return f"{self.nom} - {self.montant}€"
    
class StatutDepense(models.Model):
    depense_recurrente = models.ForeignKey(DepenseRecurrente, on_delete=models.CASCADE)
    date = models.DateField()
    est_paye = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.depense_recurrente} - Payé : {self.est_paye}"