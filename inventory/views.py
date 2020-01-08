from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets, status
from rest_framework.response import Response

# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.decorators import action

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


class main(LoginRequiredMixin, View):
    template_name = "inventory/main.html"
    model = Item

    def get(self, request, *args, **kwargs):
        form = ItemForm()
        return render(request, 'inventory/main.html', {'form': form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return HttpResponse('POST request!')


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all().exclude(active=False).order_by("position")
    serializer_class = ItemSerializer

    # def list(self, request):
    #     print("List", request.GET)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        print("Create:", serializer, request)
        if serializer.is_valid():
            print("IS VALID!", serializer)
            self.perform_create(serializer)
            # headers = self.get_success_headers(serializer.data)
            return Response({'success': True, 'type': 'new', 'item': serializer.data})
        else:
            print(serializer.errors)
            errors = serializer.errors
            return Response({'success': False, 'errors': errors, 'item': serializer.data})
        print("Create", request.POST)

    def perform_create(self, serializer):
        serializer.validated_data['position'] = Item().next_position
        serializer.save()

    def retrieve(self, request, pk=None):
        print("Retrieve", request.POST)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True})

    def update(self, request, pk=None):
        print("Updating!", request.data)
        instance = self.get_object()
        print(instance)
        serializer = ItemSerializer(
            instance=instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("DATA", instance.__dict__)
        return Response({'success': True, 'item': serializer.data})


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
