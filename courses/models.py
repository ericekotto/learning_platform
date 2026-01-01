# -*- coding: utf-8 -*-
"""
Modèles pour les cours, exercices et scores
"""

from django.db import models
from django.conf import settings

class Course(models.Model):
    """
    Modèle représentant un cours/module d'apprentissage
    """
    COURSE_TYPES = (
        ('variables', 'Variables et instructions de base'),
        ('conditionals', 'Instructions conditionnelles'),
        ('loops', 'Structures itératives'),
        ('functions', 'Fonctions et procédures'),
    )
    
    title = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )
    
    course_type = models.CharField(
        max_length=20,
        choices=COURSE_TYPES,
        unique=True,
        verbose_name="Type de cours"
    )
    
    description = models.TextField(
        verbose_name="Description"
    )
    
    content = models.TextField(
        verbose_name="Contenu du cours"
    )
    
    importance = models.TextField(
        verbose_name="Importance de ce concept",
        help_text="Pourquoi ce concept est important"
    )
    
    when_to_use = models.TextField(
        verbose_name="Quand utiliser",
        help_text="Dans quelles situations utiliser ce concept"
    )
    
    possible_operations = models.TextField(
        verbose_name="Opérations possibles",
        help_text="Ce qu'on peut faire avec ce concept"
    )
    
    impossible_operations = models.TextField(
        verbose_name="Opérations impossibles",
        help_text="Ce qu'on ne peut pas faire"
    )
    
    order = models.IntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )
    
    youtube_search_query = models.CharField(
        max_length=200,
        verbose_name="Requête YouTube",
        help_text="Terme de recherche pour les vidéos YouTube"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def get_exercises(self):
        """Retourne tous les exercices de ce cours"""
        return self.exercises.all()
    
    def get_student_count(self):
        """Retourne le nombre d'étudiants ayant fait des exercices"""
        return StudentScore.objects.filter(
            exercise__course=self
        ).values('student').distinct().count()


class Exercise(models.Model):
    """
    Modèle représentant un exercice
    """
    DIFFICULTY_CHOICES = (
        ('easy', 'Facile'),
        ('medium', 'Moyen'),
        ('hard', 'Difficile'),
    )
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='exercises',
        verbose_name="Cours"
    )
    
    title = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )
    
    question = models.TextField(
        verbose_name="Énoncé"
    )
    
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='easy',
        verbose_name="Difficulté"
    )
    
    points = models.IntegerField(
        default=10,
        verbose_name="Points"
    )
    
    order = models.IntegerField(
        default=0,
        verbose_name="Ordre"
    )
    
    # Choix multiples
    option_a = models.CharField(
        max_length=500,
        verbose_name="Option A"
    )
    
    option_b = models.CharField(
        max_length=500,
        verbose_name="Option B"
    )
    
    option_c = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Option C"
    )
    
    option_d = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Option D"
    )
    
    correct_answer = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
        verbose_name="Réponse correcte"
    )
    
    explanation = models.TextField(
        verbose_name="Explication",
        help_text="Explication de la réponse correcte"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = "Exercice"
        verbose_name_plural = "Exercices"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
    def get_success_rate(self):
        """Calcule le taux de réussite de cet exercice"""
        attempts = StudentScore.objects.filter(exercise=self)
        if attempts.count() == 0:
            return 0
        successful = attempts.filter(score__gte=self.points).count()
        return round((successful / attempts.count()) * 100, 2)


class StudentScore(models.Model):
    """
    Modèle pour stocker les scores des étudiants
    """
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scores',
        verbose_name="Étudiant"
    )
    
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='student_scores',
        verbose_name="Exercice"
    )
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='student_scores',
        verbose_name="Cours"
    )
    
    score = models.IntegerField(
        verbose_name="Score obtenu"
    )
    
    max_score = models.IntegerField(
        verbose_name="Score maximum"
    )
    
    answer_given = models.CharField(
        max_length=1,
        verbose_name="Réponse donnée"
    )
    
    is_correct = models.BooleanField(
        default=False,
        verbose_name="Réponse correcte ?"
    )
    
    attempt_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de tentative"
    )
    
    class Meta:
        verbose_name = "Score étudiant"
        verbose_name_plural = "Scores étudiants"
        ordering = ['-attempt_date']
    
    def __str__(self):
        return f"{self.student.username} - {self.exercise.title} - {self.score}/{self.max_score}"


class InstructorFeedback(models.Model):
    """
    Modèle pour les commentaires des encadreurs
    """
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feedbacks_given',
        verbose_name="Encadreur"
    )
    
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feedbacks_received',
        verbose_name="Étudiant"
    )
    
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name="Exercice"
    )
    
    feedback_text = models.TextField(
        verbose_name="Commentaire"
    )
    
    feedback_type = models.CharField(
        max_length=20,
        choices=[
            ('encouragement', 'Encouragement'),
            ('correction', 'Correction'),
            ('congratulation', 'Félicitation'),
        ],
        default='correction',
        verbose_name="Type de feedback"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    
    class Meta:
        verbose_name = "Commentaire encadreur"
        verbose_name_plural = "Commentaires encadreurs"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Feedback de {self.instructor.username} pour {self.student.username}"