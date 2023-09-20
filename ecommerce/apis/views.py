from rest_framework import filters, viewsets
from . models import *
from .serilizer import *


class categoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer


class attributeViewSets(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerilizer


class brandViewSets(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerilizer


class productsViewSets(viewsets.ModelViewSet):
    queryset = InHouseProducts.objects.all()
    serializer_class = InHouseSerilizer
    filter_backends = [filters.SearchFilter]  # Add the SearchFilter backend
    search_fields = ['name', 'description'] 