from .models import Item, Category, Vendor
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    # def to_representation(self, data):
    #     res = super(CategorySerializer, self).to_representation(data)
    #     return {res['id']: res}

    class Meta:
        model = Category
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    # Custom data
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    # def to_representation(self, data):
    #     res = super(ItemSerializer, self).to_representation(data)
    #     return {res['id']: res}

    class Meta:
        model = Item
        fields = "__all__"
