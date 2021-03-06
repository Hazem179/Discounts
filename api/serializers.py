from rest_framework import serializers
from shop.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "shop",
        ]