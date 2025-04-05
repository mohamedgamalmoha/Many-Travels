from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.utils import is_expanded
from rest_flex_fields.views import FlexFieldsMixin
from rest_flex_fields.filter_backends import FlexFieldsFilterBackend

from locations.models import Country, City, State
from locations.api.serializers import CountrySerializer, CitySerializer, StateSerializer


class CountryViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]
    filter_backends = [FlexFieldsFilterBackend] + api_settings.DEFAULT_FILTER_BACKENDS
    permit_list_expands = ['cities']
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'cities'):
            queryset = queryset.select_related('cities')
        return queryset


class CityViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]
    filter_backends = [FlexFieldsFilterBackend] + api_settings.DEFAULT_FILTER_BACKENDS
    permit_list_expands = ['states', 'country']
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'states'):
            queryset = queryset.select_related('states')
        return queryset


class StateViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [AllowAny]
    filter_backends = [FlexFieldsFilterBackend] + api_settings.DEFAULT_FILTER_BACKENDS
    permit_list_expands = ['city']
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'city'):
            queryset = queryset.prefetch_related('city')
        return queryset
