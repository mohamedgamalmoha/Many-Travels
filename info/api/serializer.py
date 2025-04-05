from django.contrib.auth.backends import get_user_model

from rest_framework import serializers

from agency.constants import DEFAULT_HEADER_IMAGE_URL
from agency.api.mixins import DefaultImageSerializerMixin
from info.models import MainInfo, SocialMedia, HeaderImage, Service, AboutUs, Theme, ContactUs
from info.constant import (DEFAULT_INFO_IMAGE_URL, DEFAULT_SERVICE_IMAGE_URL, DEFAULT_THEME_IMAGE_URL,
                        DEFAULT_MISSING_INFO_IMAGE_URL)


User = get_user_model()


class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialMedia
        exclude = ('info', )
        read_only_fields = ('create_at', 'update_at')


class HeaderImageSerializer(DefaultImageSerializerMixin, serializers.ModelSerializer):
    default_image_url = DEFAULT_HEADER_IMAGE_URL

    class Meta:
        model = HeaderImage
        exclude = ('info', )
        read_only_fields = ('create_at', 'update_at')


class MainInfoSerializer(DefaultImageSerializerMixin, serializers.ModelSerializer):
    default_image_url = DEFAULT_INFO_IMAGE_URL
    images = HeaderImageSerializer(many=True, source='header_images')
    links = SocialMediaSerializer(many=True, source='social_media_links')

    class Meta:
        model = MainInfo
        exclude = ()
        read_only_fields = ('create_at', 'update_at')


class ServiceSerializer(DefaultImageSerializerMixin, serializers.ModelSerializer):
    default_image_url = DEFAULT_SERVICE_IMAGE_URL

    class Meta:
        model = Service
        exclude = ()
        read_only_fields = ('create_at', 'update_at')


class AboutUsSerializer(DefaultImageSerializerMixin, serializers.ModelSerializer):
    default_image_url = DEFAULT_MISSING_INFO_IMAGE_URL

    class Meta:
        model = AboutUs
        exclude = ()
        read_only_fields = ('create_at', 'update_at')


class ThemeSerializer(DefaultImageSerializerMixin, serializers.ModelSerializer):
    default_image_url = DEFAULT_THEME_IMAGE_URL

    class Meta:
        model = Theme
        exclude = ()
        read_only_fields = ('create_at', 'update_at')


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        exclude = ()
        read_only_fields = ('create_at', 'update_at')
