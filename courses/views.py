# -*- coding: utf-8 -*-
"""
Vues pour la gestion des cours et exercices
VERSION AVEC VIDÉOS YOUTUBE INTÉGRÉES (sans besoin d'API)
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q
from .models import Course, Exercise, StudentScore, InstructorFeedback
from django.conf import settings


def get_youtube_videos_fallback(course_type):
    """
    Retourne des vidéos YouTube recommandées pour chaque cours
    Sans besoin d'API - Vidéos présélectionnées
    """
    videos_by_course = {
        'variables': [
            {
                'id': 'rfscVS0vtbw',
                'title': 'Les Variables en Programmation - Cours Complet',
                'description': 'Apprenez les bases des variables en algorithmique',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/watch?v=rfscVS0vtbw'
            },
            {
                'id': 'hugoparicio/algorithmique-variables',
                'title': 'Variables et Types de Données - Algorithmique',
                'description': 'Comprendre les types de données et les variables',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=algorithmique+variables+d%C3%A9butant+fran%C3%A7ais'
            },
            {
                'id': 'search-variables',
                'title': 'Cours Algorithmique - Variables',
                'description': 'Tutoriel complet sur les variables',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=cours+variables+programmation+français'
            },
        ],
        'conditionals': [
            {
                'id': 'conditional-1',
                'title': 'Les Structures Conditionnelles - if, else, elif',
                'description': 'Apprenez à utiliser les conditions dans vos programmes',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=algorithmique+conditions+if+else+français'
            },
            {
                'id': 'conditional-2',
                'title': 'Structures de Contrôle - Algorithmique',
                'description': 'Maîtrisez les instructions conditionnelles',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=cours+conditions+programmation+débutant'
            },
            {
                'id': 'conditional-3',
                'title': 'Les Tests et Conditions en Programmation',
                'description': 'Tutoriel sur les structures de contrôle',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=structures+conditionnelles+algorithmique'
            },
        ],
        'loops': [
            {
                'id': 'loops-1',
                'title': 'Les Boucles for et while - Algorithmique',
                'description': 'Comprendre les structures itératives',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=boucles+for+while+algorithmique+français'
            },
            {
                'id': 'loops-2',
                'title': 'Structures Itératives - Cours Complet',
                'description': 'Maîtrisez les boucles en programmation',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=cours+boucles+programmation+débutant'
            },
            {
                'id': 'loops-3',
                'title': 'Les Répétitions en Algorithmique',
                'description': 'Tutoriel sur les structures répétitives',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=structures+itératives+algorithmique'
            },
        ],
        'functions': [
            {
                'id': 'functions-1',
                'title': 'Les Fonctions et Procédures - Algorithmique',
                'description': 'Apprenez à créer des fonctions réutilisables',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=fonctions+procédures+algorithmique+français'
            },
            {
                'id': 'functions-2',
                'title': 'Programmation Modulaire - Les Fonctions',
                'description': 'Comprendre les fonctions et leur utilité',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=cours+fonctions+programmation+débutant'
            },
            {
                'id': 'functions-3',
                'title': 'Créer des Fonctions - Tutoriel Complet',
                'description': 'Guide pratique sur les fonctions',
                'thumbnail': 'https://img.youtube.com/vi/rfscVS0vtbw/mqdefault.jpg',
                'url': 'https://www.youtube.com/results?search_query=créer+fonctions+algorithmique'
            },
        ],
    }
    
    return videos_by_course.get(course_type, [])


def get_youtube_videos(query, course_type=None, max_results=5):
    """
    Récupère les vidéos YouTube pour une requête donnée
    Essaie d'abord l'API, sinon utilise les vidéos par défaut
    """
    # Si on a un course_type, on peut utiliser les vidéos préconfigurées
    if course_type:
        fallback_videos = get_youtube_videos_fallback(course_type)
        if fallback_videos:
            return fallback_videos[:max_results]
    
    # Tentative d'utilisation de l'API YouTube si configurée
    try:
        from googleapiclient.discovery import build
        
        if not settings.YOUTUBE_API_KEY or settings.YOUTUBE_API_KEY == 'VOTRE_CLE_API_YOUTUBE_ICI':
            # Pas de clé API configurée, utiliser les vidéos par défaut
            if course_type:
                return get_youtube_videos_fallback(course_type)
            return []
        
        youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
        
        search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=max_results,
            type='video',
            relevanceLanguage='fr'
        ).execute()
        
        videos = []
        for item in search_response.get('items', []):
            video = {
                'id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            videos.append(video)
        
        return videos
    except Exception as e:
        print(f"Erreur YouTube API: {e}")
        # En cas d'erreur, utiliser les vidéos par défaut
        if course_type:
            return get_youtube_videos_fallback(course_type)
        return []


@login_required
def home(request):
    """
    Page d'accueil affichant tous les cours
    """
    courses = Course.objects.all().order_by('order')
    
    # Statistiques pour l'étudiant connecté
    user_stats = None
    if request.user.is_student():
        total_score = request.user.get_total_score()
        completion = request.user.get_completion_percentage()
        exercises_done = StudentScore.objects.filter(student=request.user).count()
        
        user_stats = {
            'total_score': total_score,
            'completion': completion,
            'exercises_done': exercises_done,
        }
    
    context = {
        'courses': courses,
        'user_stats': user_stats,
    }
    
    return render(request, 'courses/home.html', context)


@login_required
def course_detail(request, course_id):
    """
    Page détaillée d'un cours avec son contenu et ses exercices
    """
    course = get_object_or_404(Course, id=course_id)
    exercises = course.get_exercises()
    
    # Récupérer les vidéos YouTube (avec fallback automatique)
    youtube_videos = get_youtube_videos(
        course.youtube_search_query, 
        course_type=course.course_type,
        max_results=6
    )
    
    # Scores de l'étudiant pour ce cours
    user_scores = None
    if request.user.is_student():
        user_scores = StudentScore.objects.filter(
            student=request.user,
            course=course
        ).select_related('exercise')
    
    context = {
        'course': course,
        'exercises': exercises,
        'youtube_videos': youtube_videos,
        'user_scores': user_scores,
    }
    
    return render(request, 'courses/course_detail.html', context)


@login_required
def exercise_view(request, exercise_id):
    """
    Vue pour afficher et répondre à un exercice
    """
    exercise = get_object_or_404(Exercise, id=exercise_id)
    course = exercise.course
    
    # Vérifier que c'est un étudiant
    if not request.user.is_student():
        messages.error(request, "Seuls les étudiants peuvent faire les exercices.")
        return redirect('courses:course_detail', course_id=course.id)
    
    # Vérifier si l'étudiant a déjà répondu
    previous_attempt = StudentScore.objects.filter(
        student=request.user,
        exercise=exercise
    ).first()
    
    # Traiter la soumission
    if request.method == 'POST':
        answer = request.POST.get('answer', '').upper()
        
        if not answer:
            messages.error(request, "Veuillez sélectionner une réponse.")
        else:
            # Vérifier la réponse
            is_correct = (answer == exercise.correct_answer)
            score = exercise.points if is_correct else 0
            
            # Enregistrer le score
            StudentScore.objects.create(
                student=request.user,
                exercise=exercise,
                course=course,
                score=score,
                max_score=exercise.points,
                answer_given=answer,
                is_correct=is_correct
            )
            
            if is_correct:
                messages.success(request, f"Bravo ! Vous avez gagné {score} points !")
            else:
                messages.warning(request, f"Réponse incorrecte. La bonne réponse était : {exercise.correct_answer}")
            
            return redirect('courses:exercise_result', exercise_id=exercise.id)
    
    # Récupérer les feedbacks des encadreurs
    feedbacks = InstructorFeedback.objects.filter(
        student=request.user,
        exercise=exercise
    ).select_related('instructor')
    
    context = {
        'exercise': exercise,
        'course': course,
        'previous_attempt': previous_attempt,
        'feedbacks': feedbacks,
    }
    
    return render(request, 'courses/exercise.html', context)


@login_required
def exercise_result(request, exercise_id):
    """
    Affiche le résultat d'un exercice
    """
    exercise = get_object_or_404(Exercise, id=exercise_id)
    
    # Récupérer la dernière tentative
    last_attempt = StudentScore.objects.filter(
        student=request.user,
        exercise=exercise
    ).order_by('-attempt_date').first()
    
    if not last_attempt:
        messages.error(request, "Vous n'avez pas encore répondu à cet exercice.")
        return redirect('courses:exercise', exercise_id=exercise_id)
    
    context = {
        'exercise': exercise,
        'attempt': last_attempt,
    }
    
    return render(request, 'courses/exercise_result.html', context)


@login_required
def leaderboard(request):
    """
    Classement général des étudiants
    """
    # Classement par score total
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    students = User.objects.filter(user_type='student').annotate(
        total_score=Sum('scores__score'),
        exercises_done=Count('scores')
    ).order_by('-total_score')
    
    # Classement par cours
    courses = Course.objects.all()
    course_leaderboards = {}
    
    for course in courses:
        top_students = User.objects.filter(
            user_type='student',
            scores__course=course
        ).annotate(
            course_score=Sum('scores__score', filter=Q(scores__course=course))
        ).order_by('-course_score')[:10]
        
        course_leaderboards[course] = top_students
    
    context = {
        'students': students,
        'course_leaderboards': course_leaderboards,
    }
    
    return render(request, 'courses/leaderboard.html', context)


@login_required
def my_progress(request):
    """
    Page de progression personnelle de l'étudiant
    """
    if not request.user.is_student():
        messages.error(request, "Cette page est réservée aux étudiants.")
        return redirect('courses:home')
    
    # Scores par cours
    courses = Course.objects.all()
    progress_data = []
    
    for course in courses:
        scores = StudentScore.objects.filter(
            student=request.user,
            course=course
        )
        
        total_score = scores.aggregate(Sum('score'))['score__sum'] or 0
        exercises_done = scores.count()
        total_exercises = course.exercises.count()
        
        progress_data.append({
            'course': course,
            'total_score': total_score,
            'exercises_done': exercises_done,
            'total_exercises': total_exercises,
            'completion': round((exercises_done / total_exercises * 100), 2) if total_exercises > 0 else 0
        })
    
    # Feedbacks reçus
    feedbacks = InstructorFeedback.objects.filter(
        student=request.user
    ).select_related('instructor', 'exercise').order_by('-created_at')[:10]
    
    context = {
        'progress_data': progress_data,
        'feedbacks': feedbacks,
        'total_score': request.user.get_total_score(),
    }
    
    return render(request, 'courses/my_progress.html', context)