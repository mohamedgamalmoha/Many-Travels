from django.db import models

from django_filters import rest_framework as filters

from agency.models import Agency, Travel


class AgencyFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='custom_search', label="Search in name & description")

    class Meta:
        model = Agency
        fields = ('search', 'name', 'description', 'country', 'city', 'state', 'is_active')

    def custom_search(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) | models.Q(description__icontains=value)
        )


class TravelFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='custom_search', label="Search in name & description")
    start_date = filters.DateFilter(field_name='start_date', lookup_expr='gte', label='Start Date After')
    end_date = filters.DateFilter(field_name='end_date', lookup_expr='lte', label='End Date Before')
    price = filters.RangeFilter(field_name='price', label='Price Range')

    class Meta:
        model = Travel
        fields = ('search', 'agency', 'origin_country', 'origin_city', 'destination_country', 'destination_city',
                  'travel_type', 'housing_type', 'start_date', 'end_date', 'tags', 'price', 'is_active', 'is_featured')

    def custom_search(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) | models.Q(description__icontains=value)
        )
