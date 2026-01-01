# -*- coding: utf-8 -*-
"""
Modèles de données pour la gestion des utilisateurs
- User : Utilisateur personnalisé (étudiant ou encadreur)
- UserProfile : Profil étendu de l'utilisateur
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Modèle utilisateur personnalisé
    Hérite de AbstractUser pour garder les fonctionnalités de base
    """
    USER_TYPE_CHOICES = (
        ('student', 'Étudiant'),
        ('instructor', 'Encadreur'),
    )
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='student',
        verbose_name="Type d'utilisateur"
    )
    
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Téléphone"
    )
    
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date de naissance"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'inscription"
    )
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_user_type_display()})"
    
    def is_student(self):
        """Vérifie si l'utilisateur est un étudiant"""
        return self.user_type == 'student'
    
    def is_instructor(self):
        """Vérifie si l'utilisateur est un encadreur"""
        return self.user_type == 'instructor'
    
    def get_total_score(self):
        """Calcule le score total de l'étudiant"""
        if self.is_student():
            from courses.models import StudentScore
            scores = StudentScore.objects.filter(student=self)
            return sum(score.score for score in scores)
        return 0
    
    def get_completion_percentage(self):
        """Calcule le pourcentage de complétion des cours"""
        if self.is_student():
            from courses.models import Course, StudentScore
            total_courses = Course.objects.count()
            completed = StudentScore.objects.filter(
                student=self
            ).values('course').distinct().count()
            
            if total_courses > 0:
                return round((completed / total_courses) * 100, 2)
        return 0


class UserProfile(models.Model):
    """
    Profil étendu de l'utilisateur
    Stocke des informations supplémentaires
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    bio = models.TextField(
        blank=True,
        verbose_name="Biographie"
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="Photo de profil"
    )
    
    level = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Niveau d'études"
    )
    
    school = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="École/Université"
    )
    
    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name_plural = "Profils utilisateurs"
    
    def __str__(self):
        return f"Profil de {self.user.username}"