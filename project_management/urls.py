"""
URL configuration for project_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from app.views import *
from django.views.generic import TemplateView


router = routers.DefaultRouter()


router.register(r'projects', ProjectViewSet)
router.register(r'projectmembers', ProjectMemberViewSet)
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'projects/(?P<project_id>\d+)/tasks', TaskViewSet, basename='project-task')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'tasks/(?P<task_id>\d+)/comments', CommentViewSet, basename='task-comment')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("", include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]