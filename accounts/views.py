# -*- coding: utf-8 -*-
"""
Vues pour l'authentification et la gestion des comptes
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrationForm, InstructorRegistrationForm, LoginForm
from .models import UserProfile


def register_student(request):
    """
    Inscription d'un nouvel étudiant
    """
    if request.user.is_authenticated:
        return redirect('courses:home')
    
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'student'
            user.save()
            
            # Créer le profil
            UserProfile.objects.create(user=user)
            
            # Connecter automatiquement
            login(request, user)
            messages.success(request, "Inscription réussie ! Bienvenue sur la plateforme.")
            return redirect('courses:home')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'accounts/register_student.html', {'form': form})


def register_instructor(request):
    """
    Inscription d'un nouvel encadreur
    """
    if request.user.is_authenticated:
        return redirect('courses:home')
    
    if request.method == 'POST':
        form = InstructorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'instructor'
            user.save()
            
            # Créer le profil
            UserProfile.objects.create(user=user)
            
            # Connecter automatiquement
            login(request, user)
            messages.success(request, "Inscription réussie ! Bienvenue encadreur.")
            return redirect('instructor:dashboard')
    else:
        form = InstructorRegistrationForm()
    
    return render(request, 'accounts/register_instructor.html', {'form': form})


def login_view(request):
    """
    Connexion des utilisateurs
    """
    if request.user.is_authenticated:
        if request.user.is_instructor():
            return redirect('instructor:dashboard')
        return redirect('courses:home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue {user.get_full_name()} !")
                
                # Rediriger selon le type d'utilisateur
                if user.is_instructor():
                    return redirect('instructor:dashboard')
                return redirect('courses:home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    """
    Déconnexion
    """
    logout(request)
    messages.info(request, "Vous êtes déconnecté. À bientôt !")
    return redirect('accounts:login')


@login_required
def dashboard(request):
    """
    Tableau de bord utilisateur
    """
    if request.user.is_instructor():
        return redirect('instructor:dashboard')
    
    return redirect('courses:home')


@login_required
def profile(request):
    """
    Profil utilisateur
    """
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    context = {
        'profile': profile,
    }
    
    return render(request, 'accounts/profile.html', context)