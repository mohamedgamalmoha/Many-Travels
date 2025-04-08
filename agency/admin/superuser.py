from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from agency.models import  WorkTime, HeaderImage, SocialMediaLink


class WorkTimeInline(admin.TabularInline):
    model = WorkTime
    extra = 1
    min = 0
    show_change_link = False


class HeaderImageInline(admin.TabularInline):
    model = HeaderImage
    extra = 1
    min = 0
    readonly_fields = ('create_at', 'update_at')
    show_change_link = False


class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1
    min = 0
    readonly_fields = ('create_at', 'update_at')
    show_change_link = False


class TagAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'is_active', 'create_at', 'update_at')
    list_filter = ('is_active', )
    search_fields = ('name', )
    fieldsets = (
        (_('Main Info'), {'fields': ('name', 'icon', 'order', 'is_active')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


class AgencyAdmin(TranslationAdmin):
    list_display = ('order', 'name', 'is_active', 'create_at', 'update_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    readonly_fields = ('create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('owner', ('name', 'slug'), 'description', 'email', 'contact_number',
                                     'whatsapp_number')}),
        (_('More Info'), {'fields': ('country','city', 'state', 'is_active', 'order', 'image')}),
        (_('Theme'), {'fields': ('theme', 'primary_color', 'border_color')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )
    inlines = [WorkTimeInline, HeaderImageInline, SocialMediaLinkInline]


class TravelAdmin(TranslationAdmin):
    list_display = ('name', 'agency', 'is_active', 'create_at', 'update_at')
    list_filter = ('is_active','travel_type', 'housing_type')
    search_fields = ('name', 'description')
    readonly_fields = ('create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('agency', 'name', 'description', 'price', 'after_sale_price')}),
        (_('Location'), {'fields': ('origin_country', 'origin_city', 'destination_country', 'destination_city')}),
        (_('Date'), {'fields': ('start_date', 'end_date', 'duration')}),
        (_('More Info'), {'fields': ('travel_type', 'housing_type', 'tags', 'is_featured', 'is_active',  'order',
                                     'image')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )
