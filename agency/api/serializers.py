from rest_framework.serializers import  ModelSerializer
from rest_flex_fields.serializers import FlexFieldsModelSerializer

from agency.models import Agency, WorkTime, HeaderImage, SocialMediaLink, Tag, Travel


class AgencySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Agency
        exclude = ()
        read_only_fields = ('create_at', 'update_at')
        expandable_fields = {
            'work_times': ('agency.api.serializers.WorkTimeSerializer', {'many': True, "omit": ["agency"]}),
            'header_images': ('agency.api.serializers.HeaderImageSerializer', {'many': True, "omit": ["agency"]}),
            'social_media_links': ('agency.api.serializers.SocialMediaLinkSerializer', {'many': True,
                                                                                        "omit": ["agency"]}),
            'travels': ('agency.api.serializers.TravelSerializer', {'many': True, "omit": ["agency"]}),
            'country': ('locations.api.serializers.CountrySerializer', {'many': False, "omit": ["agencies"]}),
            'city': ('locations.api.serializers.CitySerializer', {'many': False, "omit": ["agencies"]}),
            'state': ('locations.api.serializers.StateSerializer', {'many': False, "omit": ["agencies"]})
        }


class WorkTimeSerializer(ModelSerializer):

    class Meta:
        model = WorkTime
        exclude = ('agency', )


class HeaderImageSerializer(ModelSerializer):

    class Meta:
        model = HeaderImage
        exclude = ('agency', )
        read_only_fields = ('create_at', 'update_at')


class SocialMediaLinkSerializer(ModelSerializer):

    class Meta:
        model = SocialMediaLink
        exclude = ('agency', )
        read_only_fields = ('create_at', 'update_at')


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        exclude = ()
        read_only_fields = ('create_at', 'update_at')


class TravelSerializer(ModelSerializer):

    class Meta:
        model = Travel
        exclude = ()
        read_only_fields = ('create_at', 'update_at')
        expandable_fields = {
            'agency': ('agency.api.serializers.AgencySerializer', {'many': False, "omit": ["travels"]}),
            'tags': ('agency.api.serializers.TagSerializer', {'many': True, "omit": ["travel"]}),
            'origin_country': ('locations.api.serializers.CountrySerializer', {'many': False,
                                                                               "omit": ["origin_travels"]}),
            'origin_city': ('locations.api.serializers.CitySerializer', {'many': False, "omit": ["origin_travels"]}),
            'destination_country': ('locations.api.serializers.CountrySerializer', {'many': False,
                                                                                    "omit": ["destination_travels"]}),
            'destination_city': ('locations.api.serializers.CitySerializer', {'many': False,
                                                                              "omit": ["destination_travels"]})

        }
