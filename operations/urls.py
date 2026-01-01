"""
Ce fichier définit toutes les URLs de notre application d'apprentissage.
Chaque path() associe une URL à une vue (fonction qui génère la page).
"""
from django.urls import path
from . import views

app_name = 'operations'  # Namespace pour éviter les conflits

urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),
    
    # Page d'information sur les types de données
    path('types-info/', views.types_info, name='types_info'),
    
    # Pages pour chaque opération
    path('addition/', views.operation_view, {'operation': 'addition'}, name='addition'),
    path('soustraction/', views.operation_view, {'operation': 'soustraction'}, name='soustraction'),
    path('multiplication/', views.operation_view, {'operation': 'multiplication'}, name='multiplication'),
    path('division/', views.operation_view, {'operation': 'division'}, name='division'),
    path('modulo/', views.operation_view, {'operation': 'modulo'}, name='modulo'),
    path('concatenation/', views.operation_view, {'operation': 'concatenation'}, name='concatenation'),
    path('comparaison/', views.operation_view, {'operation': 'comparaison'}, name='comparaison'),
]