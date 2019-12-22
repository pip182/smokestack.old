from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class main(View, LoginRequiredMixin):
    template_name = "tasks/main.html"
    model = Task

    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/main.html', {'tasks': Task.objects.all()})

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')


# REST Framework Views
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
