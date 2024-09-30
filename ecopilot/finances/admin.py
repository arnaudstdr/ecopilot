from django.contrib import admin
from .models import Revenu, DepenseRecurrente, DepensePonctuelle, StatutDepense

# Register your models here.
admin.site.register(Revenu)
admin.site.register(DepenseRecurrente)
admin.site.register(DepensePonctuelle)
admin.site.register(StatutDepense)
