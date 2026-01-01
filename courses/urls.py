# ========================================
# courses/urls.py
# ========================================
"""
URLs pour les cours et exercices
"""
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.home, name='home'),
    path('cours/<int:course_id>/', views.course_detail, name='course_detail'),
    path('exercice/<int:exercise_id>/', views.exercise_view, name='exercise'),
    path('exercice/<int:exercise_id>/resultat/', views.exercise_result, name='exercise_result'),
    path('classement/', views.leaderboard, name='leaderboard'),
    path('ma-progression/', views.my_progress, name='my_progress'),
]
