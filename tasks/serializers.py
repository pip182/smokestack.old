from rest_framework import serializers
from .models import Task, TaskCategory


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
