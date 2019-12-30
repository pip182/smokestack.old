from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms

from .models import Item, Category, Vendor
from .serializers import ItemSerializer, VendorSerializer, CategorySerializer


class ItemForm(forms.ModelForm):
    """Form definition for Item."""

    class Meta:
        """Meta definition for Itemform."""

        model = Item
        widgets = {
            # 'notes': SummernoteInplaceWidget(),
        }
        fields = ('__all__')


class main(View, LoginRequiredMixin):
    template_name = "inventory/main.html"
    model = Item

    def get(self, request, *args, **kwargs):
        form = ItemForm()
        return render(request, 'inventory/main.html',
            {'items': Item.objects.all(), 'form': form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return HttpResponse('POST request!')


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request):
        print("Create", request.POST)

    def retrieve(self, request, pk=None):
        print("Retrieve", request.POST)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = ItemSerializer(
            instance=instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
