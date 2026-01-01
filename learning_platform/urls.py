# -*- coding: utf-8 -*-
# ========================================
# learning_platform/urls.py (URLs principales)
# ========================================
"""
URLs principales du projet
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('cours/', include('courses.urls')),
    path('encadreur/', include('instructor.urls')),
    path('operations/', include('operations.urls')),
]

# Servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





# ========================================
