from django.test import TestCase
from django.contrib.auth.models import User
from .models import Revenu

# Create your tests here.
class RevenuTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        Revenu.objects.create(utilisateur=user, montant=1000, source="Salaire", date_reception="2024-01-01")

    def test_revenu(self):
        user = User.objects.get(username="testuser")
        revenu = Revenu.objects.get(utilisateur=user)
        self.assertEqual(revenu.montant, 1000)