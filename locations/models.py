from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Country Name'))
    code = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('Country Code'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create At'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update At'))

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name='cities',
        verbose_name=_('Country')
    )
    name = models.CharField(max_length=255, verbose_name=_('City Name'))
    code = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('City Code'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create At'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update At'))

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return self.name


class State(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        related_name='states',
        verbose_name=_('City')
    )
    name = models.CharField(max_length=255, verbose_name=_('State Name'))
    code = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('State Code'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create At'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update At'))

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        ordering = ('-create_at', '-update_at')

    def __str__(self):
        return self.name
