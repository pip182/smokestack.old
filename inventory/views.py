from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin


from rest_framework import viewsets

from .models import Item
from .serializers import ItemSerializer
# Create your views here.


class main(View, LoginRequiredMixin):
    template_name = "inventory/main.html"
    model = Item

    def get(self, request, *args, **kwargs):
        return render(request, 'inventory/main.html', {'items': Item.objects.all()})

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
