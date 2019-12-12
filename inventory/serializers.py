from .models import Item, Category, Vendor
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    # Represent the relationshit
    vendor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Item
        fields = ['name', 'price', 'current_quantity', 'vendor']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
