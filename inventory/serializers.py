from .models import Item, Category, Vendor
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    # Uncomment get get all vender data instead of just the ID
    vendor = VendorSerializer()
    # vendor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Item
        fields = "__all__"
        # exclude = ["date_modified", "date_added"]
