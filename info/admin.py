from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationAdmin

from info.models import MainInfo, SocialMedia, HeaderImage, Service, AboutUs, Theme, ContactUs


class HeaderImageInlineAdmin(admin.TabularInline):
    model = HeaderImage
    readonly_fields = ('create_at', 'update_at')


class SocialMediaInlineAdmin(admin.TabularInline):
    model = SocialMedia
    readonly_fields = ('create_at', 'update_at')


class MainInfoAdmin(TranslationAdmin):
    list_display = ['__str__', 'create_at', 'update_at']
    readonly_fields = ['create_at', 'update_at']
    search_fields = ['title', 'description']
    fieldsets = (
        (_('Main Info'), {'fields': ('title', 'description', 'image')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )
    inlines = [SocialMediaInlineAdmin, HeaderImageInlineAdmin]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class ActiveTitleWithDescriptionAdmin(TranslationAdmin):
    list_display = ['__str__', 'create_at', 'update_at']
    list_filter = ['is_active']
    readonly_fields = ['create_at', 'update_at']
    search_fields = ['title', 'description']
    fieldsets = (
        (_('Main Info'), {'fields': ('title', 'description', 'image', 'is_active')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


class ThemeAdmin(ActiveTitleWithDescriptionAdmin):
    fieldsets = (
        (_('Main Info'), {'fields': ('title', 'description', 'image', 'url', 'is_active')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'create_at', 'update_at']
    list_filter = ['platform', 'is_active']
    readonly_fields = ['create_at', 'update_at']
    fieldsets = (
        (_('Main Info'), {'fields': ('platform', 'url', 'is_active')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'create_at', 'update_at')
    search_fields = ('email', 'full_name', 'message')
    readonly_fields = ['create_at', 'update_at']
    fieldsets = (
        (_('Main Info'), {'fields': ('full_name', 'email', 'phone_number', 'message')}),
        (_('Important Dates'), {'fields': ('create_at', 'update_at')}),
    )


admin.site.register(MainInfo, MainInfoAdmin)
admin.site.register(Service, ActiveTitleWithDescriptionAdmin)
admin.site.register(AboutUs, ActiveTitleWithDescriptionAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
