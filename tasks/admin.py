# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TaskComments, Task, TaskCategory


@admin.register(TaskComments)
class TaskCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_added', 'name')
    list_filter = ('date_added', 'name')
    raw_id_fields = ('sub_comments',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'assigned_by',
        'assigned_to',
        'date_due',
        'order',
        'points',
        'priority',
        'progress',
        'status',
        'title',
    )
    list_filter = ('assigned_by', 'assigned_to', 'date_due')
    raw_id_fields = ('sub_tasks',)


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title')
    raw_id_fields = ('tasks',)
