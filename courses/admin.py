# ========================================
# courses/admin.py
# ========================================
"""
Configuration de l'interface d'administration pour les cours
"""
from django.contrib import admin
from .models import Course, Exercise, StudentScore, InstructorFeedback


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_type', 'order', 'created_at')
    list_filter = ('course_type',)
    search_fields = ('title', 'description')
    ordering = ('order',)
    
    fieldsets = (
        ('Informations de base', {
            'fields': ('title', 'course_type', 'description', 'order')
        }),
        ('Contenu pédagogique', {
            'fields': ('content', 'importance', 'when_to_use')
        }),
        ('Opérations', {
            'fields': ('possible_operations', 'impossible_operations')
        }),
        ('YouTube', {
            'fields': ('youtube_search_query',)
        }),
    )


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'difficulty', 'points', 'order')
    list_filter = ('course', 'difficulty')
    search_fields = ('title', 'question')
    ordering = ('course', 'order')
    
    fieldsets = (
        ('Informations de base', {
            'fields': ('course', 'title', 'question', 'difficulty', 'points', 'order')
        }),
        ('Options de réponse', {
            'fields': ('option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
        }),
        ('Explication', {
            'fields': ('explanation',)
        }),
    )


@admin.register(StudentScore)
class StudentScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'exercise', 'score', 'max_score', 'is_correct', 'attempt_date')
    list_filter = ('is_correct', 'course', 'attempt_date')
    search_fields = ('student__username', 'student__first_name', 'student__last_name', 'exercise__title')
    date_hierarchy = 'attempt_date'
    readonly_fields = ('attempt_date',)


@admin.register(InstructorFeedback)
class InstructorFeedbackAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'student', 'exercise', 'feedback_type', 'created_at')
    list_filter = ('feedback_type', 'created_at')
    search_fields = ('instructor__username', 'student__username', 'feedback_text')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)