from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from agency.models import  WorkTime, HeaderImage, SocialMediaLink


class PermissionsAllowAllAdminMixin:

    def has_view_or_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class WorkTimeInlineCustomerAdmin(PermissionsAllowAllAdminMixin, admin.TabularInline):
    model = WorkTime
    extra = 1
    min = 0
    exclude = ('create_at', 'update_at')
    show_change_link = False


class HeaderImageInlineCustomerAdmin(PermissionsAllowAllAdminMixin, admin.TabularInline):
    model = HeaderImage
    extra = 1
    min = 0
    exclude = ('create_at', 'update_at')
    show_change_link = False


class SocialMediaLinkInlineCustomerAdmin(PermissionsAllowAllAdminMixin, admin.TabularInline):
    model = SocialMediaLink
    extra = 1
    min = 0
    exclude = ('create_at', 'update_at')
    show_change_link = False


class AgencyCustomerAdmin(PermissionsAllowAllAdminMixin, TranslationAdmin):
    list_display = ('order', 'name', 'is_active', 'create_at', 'update_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    readonly_fields = ('create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('owner', ('name', 'slug'), 'description', 'email', 'contact_number',
                                     'whatsapp_number')}),
        (_('More Info'), {'fields': ('country','city', 'state', 'is_active', 'order', 'image')}),
        (_('Theme'), {'fields': ('primary_color', 'border_color')}),
    )
    inlines = [WorkTimeInlineCustomerAdmin, HeaderImageInlineCustomerAdmin, SocialMediaLinkInlineCustomerAdmin]


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset.filter(owner=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        if not change:  # Only set owner when adding a new object
            obj.owner = request.user
        super().save_model(request, obj, form, change)


class TravelCustomerAdmin(PermissionsAllowAllAdminMixin, TranslationAdmin):
    list_display = ('name', 'agency', 'is_active', 'create_at', 'update_at')
    list_filter = ('is_active','travel_type', 'housing_type')
    search_fields = ('name', 'description')
    readonly_fields = ('create_at', 'update_at')
    fieldsets = (
        (_('Main Info'), {'fields': ('name', 'description', 'price', 'after_sale_price')}),
        (_('Location'), {'fields': ('origin_country', 'origin_city', 'destination_country', 'destination_city')}),
        (_('Date'), {'fields': ('start_date', 'end_date', 'duration')}),
        (_('More Info'), {'fields': ('travel_type', 'housing_type', 'tags', 'is_featured', 'is_active',  'order',
                                     'image')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset.filter(agency__owner__id=request.user.id)
        return queryset

    def save_model(self, request, obj, form, change):
        if not change:  # Only set owner when adding a new object
            obj.agency = request.user.agency
        super().save_model(request, obj, form, change)
