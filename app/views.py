from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = Project_member.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [AllowAny]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        if project_id:
            return Task.objects.filter(project_id=project_id)
        else:
            return Task.objects.all()

    def create(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        
        if project_id:
            request.data['project'] = project_id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        elif 'project_id' not in request.data and 'project_id' not in request.POST:
            return Response({'project': 'This field is required'}, status=status.HTTP_400_BAD_REQUEST)
        

        


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        if task_id:
            return Comment.objects.filter(task_id=task_id)
        else:
            return Comment.objects.all()

    def create(self, request, *args, **kwargs):
        task_id = self.kwargs.get('task_id')
        
        if task_id:
            request.data['task'] = task_id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        elif 'task_id' not in request.data and 'task_id' not in request.POST:
            return Response({'task': 'This field is required'}, status=status.HTTP_400_BAD_REQUEST)