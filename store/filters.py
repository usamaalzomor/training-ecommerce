from django_filters.rest_framework import FilterSet, filters
from .models import Product

class ProductFilter(FilterSet):
    min_price = filters.NumberFilter(field_name="unit_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="unit_price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['collection_id']