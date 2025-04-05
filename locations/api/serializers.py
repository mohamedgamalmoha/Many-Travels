from rest_framework import serializers

from locations.models import Country, City


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        exclude = ()
        readonly_fields = ('created_at', 'updated_at')


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        exclude = ()
        readonly_fields = ('created_at', 'updated_at')
