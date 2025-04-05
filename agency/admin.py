from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from agency.models import Agency, HeaderImage, SocialMediaLink, Tag, Travel


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


class AgencyAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'is_active', 'create_at', 'update_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    readonly_fields = ('create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('owner', ('name', 'slug'), 'email', 'contact_number', 'image', 'is_active',
                                     'order')}),
        (_('Theme'), {'fields': ('primary_color', 'border_color')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )
    inlines = [HeaderImageInline, SocialMediaLinkInline]


class TravelAdmin(admin.ModelAdmin):
    list_display = ('name', 'agency', 'is_active', 'create_at', 'update_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    readonly_fields = ('create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('agency', 'name', 'description', 'order')}),
        (_('Location'), {'fields': ('origin_country', 'origin_city', 'destination_country', 'destination_city')}),
        (_('Date'), {'fields': ('start_date', 'end_date', 'duration')}),
        (_('More Info'), {'fields': ('price', 'after_sale_price', 'tag', 'is_featured', 'is_active', 'image')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


admin.site.register(Tag, TagAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Travel, TravelAdmin)
