from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

from locations.models import Country, City


class CityInline(TranslationInlineModelAdmin):
    model = City
    extra = 1
    readonly_fields = ('create_at', 'update_at')


class CityAdmin(TranslationAdmin):
    list_display = ('name', 'code', 'country', 'create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('country', 'name', 'code')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')})
    )
    search_fields = ('name', 'code')
    list_filter = ('country', 'create_at', 'update_at')
    ordering = ('-create_at', '-update_at')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('country')


class CountryAdmin(TranslationAdmin):
    list_display = ('name', 'code', 'create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('name', 'code')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')})
    )
    search_fields = ('name', 'code')
    list_filter = ('create_at', 'update_at')
    ordering = ('-create_at', '-update_at')
    inlines = [CityInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('cities')


admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
