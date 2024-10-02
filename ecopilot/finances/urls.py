from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<int:year>/<int:month>/', views.dashboard, name='dashboard_with_date'),
    path('revenu/ajout/', views.ajout_revenu, name='ajout_revenu'),
    path('depense_recurrente/ajout/', views.ajout_depense_recurrente, name='ajout_depense_recurrente'),
    path('depense_ponctuelle/ajout/', views.ajout_depense_ponctuelle, name='ajout_depense_ponctuelle'),
    path('depense_recurrente/pointer/<int:pk>/', views.pointer_depense_recurrente, name='pointer_depense_recurrente'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]