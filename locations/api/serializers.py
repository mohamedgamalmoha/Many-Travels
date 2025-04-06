from rest_flex_fields.serializers import FlexFieldsModelSerializer

from locations.models import Country, City, State


class CountrySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Country
        exclude = ()
        read_only_fields = ('created_at', 'updated_at')
        expandable_fields = {
            'cities': ('locations.api.serializers.CitySerializer', {'many': True, "omit": ["country"]})
        }


class CitySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = City
        exclude = ()
        read_only_fields = ('created_at', 'updated_at')
        expandable_fields = {
            'country': ('locations.api.serializers.CountrySerializer', {'many': False, 'omit': ['city']}),
            'states': ('locations.api.serializers.StateSerializer', {'many': True,'omit': ['city']})
        }


class StateSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = State
        exclude = ()
        read_only_fields = ('created_at', 'updated_at')
        expandable_fields = {
            'city': ('locations.api.serializers.CitySerializer', {'many': False, 'omit': ['states']}),
        }
