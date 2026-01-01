# ==s======================================
# accounts/urls.py
# ========================================
"""
URLs pour l'authentification
"""
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('connexion/', views.login_view, name='login'),
    path('deconnexion/', views.logout_view, name='logout'),
    path('inscription/etudiant/', views.register_student, name='register_student'),
    path('inscription/encadreur/', views.register_instructor, name='register_instructor'),
    path('tableau-de-bord/', views.dashboard, name='dashboard'),
    path('profil/', views.profile, name='profile'),
]
