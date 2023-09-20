from rest_framework import serializers
from . models import *


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AttributeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"
        many = True


class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class InHouseSerilizer(serializers.ModelSerializer):
   class Meta:
        model = InHouseProducts
        fields = "__all__"
        many = True