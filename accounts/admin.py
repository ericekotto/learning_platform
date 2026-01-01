# -*- coding: utf-8 -*-
# ========================================
# accounts/admin.py
# ========================================
"""
Configuration de l'interface d'administration pour les utilisateurs
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('user_type', 'phone', 'date_of_birth')
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'school')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')





# ========================================
# instructor/admin.py
# ========================================
"""
Pas de modèles spécifiques à enregistrer pour instructor
L'application utilise les modèles de courses
"""
from django.contrib import admin

# Rien à enregistrer ici, tout est dans courses/admin.py