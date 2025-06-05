from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.settings import api_settings
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_spectacular.utils import extend_schema
from rest_flex_fields.utils import is_expanded
from rest_flex_fields.views import FlexFieldsMixin
from rest_flex_fields.filter_backends import FlexFieldsFilterBackend

from agency.models import Agency, Travel
from agency.api.filters import AgencyFilterSet, TravelFilterSet
from agency.api.serializers import AgencySerializer, TravelSerializer


class AgencyViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    filter_backends = [FlexFieldsFilterBackend] + api_settings.DEFAULT_FILTER_BACKENDS
    filterset_class = AgencyFilterSet
    permitted_expands = ['work_times', 'header_images', 'social_media_links', 'travels', 'country', 'city', 'state']
    permit_list_expands = permitted_expands
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'work_times'):
            queryset = queryset.prefetch_related('work_times')
        if is_expanded(self.request, 'header_images'):
            queryset = queryset.prefetch_related('header_images')
        if is_expanded(self.request, 'social_media_links'):
            queryset = queryset.prefetch_related('social_media_links')
        if is_expanded(self.request, 'travels'):
            queryset = queryset.prefetch_related('travels')
        if is_expanded(self.request, 'country'):
            queryset = queryset.select_related('country')
        if is_expanded(self.request, 'city'):
            queryset = queryset.select_related('city')
        if is_expanded(self.request, 'state'):
            queryset = queryset.select_related('state')
        return queryset

    @extend_schema(responses={200: TravelSerializer}, filters=True)
    @action(["GET"], detail=True, url_path='travels', queryset=Travel.objects.none(),
            serializer_class=TravelSerializer, filterset_class=TravelFilterSet)
    def travels(self, request, *args, **kwargs):
        # Create a dictionary of filter arguments using the lookup field (e.g., 'id') and its value from the URL kwargs
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}

        # Retrieve the specific Agency object that matches the filter arguments.
        # If no Agency is found, raise a 404 error.
        agency = get_object_or_404(Travel, **filter_kwargs)

        # Dynamically set the filterset class to be used for filtering travels in the current request.
        self.filterset_class = TravelFilterSet

        # Dynamically set the serializer class to ProductSerializer for serializing the response.
        self.serializer_class = TravelSerializer

        # Set the queryset to be the travels associated with the retrieved agency.
        self.queryset = agency.products.filter(is_active=True).order_by('order', '-create_at', '-update_at')

        # Delegate to the `list` method to handle filtering, pagination, and serialization of the queryset.
        return self.list(request, *args, **kwargs)


class TravelViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    filter_backends = [FlexFieldsFilterBackend] + api_settings.DEFAULT_FILTER_BACKENDS
    filterset_class = TravelFilterSet
    permitted_expands = ['agency', 'tags', 'origin_country', 'origin_city', 'destination_country',
                         'destination_city']
    permit_list_expands = permitted_expands

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_expanded(self.request, 'agency'):
            queryset = queryset.select_related('agency')
        if is_expanded(self.request, 'tags'):
            queryset = queryset.prefetch_related('tags')
        if is_expanded(self.request, 'original_country'):
            queryset = queryset.select_related('original_country')
        if is_expanded(self.request, 'original_city'):
            queryset = queryset.select_related('original_city')
        if is_expanded(self.request, 'destination_country'):
            queryset = queryset.select_related('destination_country')
        if is_expanded(self.request, 'destination_city'):
            queryset = queryset.select_related('destination_city')
        return queryset
