
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserDeleteSerializer
from django.contrib.auth import get_user_model
from .models import *


User = get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_member
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



    