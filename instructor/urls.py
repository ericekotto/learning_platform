# instructor/urls.py
# ========================================
"""
URLs pour l'espace encadreur
"""
from django.urls import path
from . import views

app_name = 'instructor'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cours/<int:course_id>/analyse/', views.course_analytics, name='course_analytics'),
    path('etudiant/<int:student_id>/', views.student_detail, name='student_detail'),
    path('etudiant/<int:student_id>/feedback/<int:exercise_id>/', views.add_feedback, name='add_feedback'),
    path('etudiants/', views.students_list, name='students_list'),
    path('classements/', views.global_leaderboard, name='global_leaderboard'),
]