# -*- coding: utf-8 -*-
"""
Vues pour l'espace encadreur
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q, Avg
from django.contrib.auth import get_user_model
from courses.models import Course, Exercise, StudentScore, InstructorFeedback

User = get_user_model()


def instructor_required(view_func):
    """
    Décorateur pour vérifier que l'utilisateur est un encadreur
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.is_instructor():
            messages.error(request, "Accès réservé aux encadreurs.")
            return redirect('courses:home')
        return view_func(request, *args, **kwargs)
    return wrapper


@instructor_required
def dashboard(request):
    """
    Tableau de bord principal de l'encadreur
    """
    # Statistiques générales
    total_students = User.objects.filter(user_type='student').count()
    total_exercises = Exercise.objects.count()
    total_attempts = StudentScore.objects.count()
    
    # Cours avec statistiques
    courses = Course.objects.annotate(
        student_count=Count('student_scores__student', distinct=True),
        avg_score=Avg('student_scores__score')
    ).order_by('order')
    
    # Top 10 étudiants globaux
    top_students = User.objects.filter(
        user_type='student'
    ).annotate(
        total_score=Sum('scores__score'),
        exercises_count=Count('scores')
    ).order_by('-total_score')[:10]
    
    # Activité récente
    recent_scores = StudentScore.objects.select_related(
        'student', 'exercise', 'course'
    ).order_by('-attempt_date')[:15]
    
    context = {
        'total_students': total_students,
        'total_exercises': total_exercises,
        'total_attempts': total_attempts,
        'courses': courses,
        'top_students': top_students,
        'recent_scores': recent_scores,
    }
    
    return render(request, 'instructor/dashboard.html', context)


@instructor_required
def course_analytics(request, course_id):
    """
    Analyse détaillée d'un cours
    """
    course = get_object_or_404(Course, id=course_id)
    
    # Top étudiants pour ce cours
    top_students = User.objects.filter(
        user_type='student',
        scores__course=course
    ).annotate(
        course_score=Sum('scores__score', filter=Q(scores__course=course)),
        exercises_done=Count('scores', filter=Q(scores__course=course))
    ).order_by('-course_score')[:20]
    
    # Statistiques par exercice
    exercises_stats = []
    for exercise in course.exercises.all():
        attempts = StudentScore.objects.filter(exercise=exercise)
        total_attempts = attempts.count()
        successful = attempts.filter(is_correct=True).count()
        success_rate = (successful / total_attempts * 100) if total_attempts > 0 else 0
        
        exercises_stats.append({
            'exercise': exercise,
            'total_attempts': total_attempts,
            'successful': successful,
            'success_rate': round(success_rate, 2)
        })
    
    context = {
        'course': course,
        'top_students': top_students,
        'exercises_stats': exercises_stats,
    }
    
    return render(request, 'instructor/course_analytics.html', context)


@instructor_required
def student_detail(request, student_id):
    """
    Détails et progression d'un étudiant
    """
    student = get_object_or_404(User, id=student_id, user_type='student')
    
    # Scores par cours
    courses_progress = []
    for course in Course.objects.all():
        scores = StudentScore.objects.filter(
            student=student,
            course=course
        )
        
        total_score = scores.aggregate(Sum('score'))['score__sum'] or 0
        exercises_done = scores.count()
        total_exercises = course.exercises.count()
        
        courses_progress.append({
            'course': course,
            'total_score': total_score,
            'exercises_done': exercises_done,
            'total_exercises': total_exercises,
            'completion': round((exercises_done / total_exercises * 100), 2) if total_exercises > 0 else 0
        })
    
    # Historique des tentatives
    attempts = StudentScore.objects.filter(
        student=student
    ).select_related('exercise', 'course').order_by('-attempt_date')[:30]
    
    # Exercices ratés
    failed_attempts = StudentScore.objects.filter(
        student=student,
        is_correct=False
    ).select_related('exercise', 'course').order_by('-attempt_date')
    
    # Feedbacks déjà donnés
    existing_feedbacks = InstructorFeedback.objects.filter(
        student=student
    ).select_related('exercise').order_by('-created_at')
    
    context = {
        'student': student,
        'courses_progress': courses_progress,
        'attempts': attempts,
        'failed_attempts': failed_attempts,
        'existing_feedbacks': existing_feedbacks,
        'total_score': student.get_total_score(),
    }
    
    return render(request, 'instructor/student_detail.html', context)


@instructor_required
def add_feedback(request, student_id, exercise_id):
    """
    Ajouter un feedback pour un étudiant
    """
    student = get_object_or_404(User, id=student_id, user_type='student')
    exercise = get_object_or_404(Exercise, id=exercise_id)
    
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback_text', '').strip()
        feedback_type = request.POST.get('feedback_type', 'correction')
        
        if feedback_text:
            InstructorFeedback.objects.create(
                instructor=request.user,
                student=student,
                exercise=exercise,
                feedback_text=feedback_text,
                feedback_type=feedback_type
            )
            messages.success(request, f"Feedback envoyé à {student.get_full_name()} !")
        else:
            messages.error(request, "Le commentaire ne peut pas être vide.")
        
        return redirect('instructor:student_detail', student_id=student_id)
    
    context = {
        'student': student,
        'exercise': exercise,
    }
    
    return render(request, 'instructor/add_feedback.html', context)


@instructor_required
def students_list(request):
    """
    Liste de tous les étudiants avec leurs statistiques
    """
    students = User.objects.filter(
        user_type='student'
    ).annotate(
        total_score=Sum('scores__score'),
        exercises_count=Count('scores')
    ).order_by('-total_score')
    
    # Filtrage par recherche
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    context = {
        'students': students,
        'search_query': search_query,
    }
    
    return render(request, 'instructor/students_list.html', context)


@instructor_required
def global_leaderboard(request):
    """
    Classement global et par catégorie
    """
    # Classement général
    general_ranking = User.objects.filter(
        user_type='student'
    ).annotate(
        total_score=Sum('scores__score'),
        exercises_count=Count('scores')
    ).order_by('-total_score')
    
    # Classement par cours
    courses_rankings = {}
    for course in Course.objects.all():
        ranking = User.objects.filter(
            user_type='student',
            scores__course=course
        ).annotate(
            course_score=Sum('scores__score', filter=Q(scores__course=course)),
            exercises_done=Count('scores', filter=Q(scores__course=course))
        ).order_by('-course_score')[:15]
        
        courses_rankings[course] = ranking
    
    context = {
        'general_ranking': general_ranking,
        'courses_rankings': courses_rankings,
    }
    
    return render(request, 'instructor/global_leaderboard.html', context)