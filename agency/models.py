from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from locations.models import Country, City
from agency.enums import SocialMediaPlatform
from agency.constants import FORCED_IMAGE_FORMAT, MAX_FILE_SIZE
from agency.validators import FileSizeValidator, validate_hex_color, validate_english_alphanum


User = get_user_model()


class Agency(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shop", verbose_name=_("Owner"))

    name = models.CharField(max_length=255, verbose_name=_("Shop Name"))
    slug = models.SlugField(max_length=255, unique=True, validators=[validate_english_alphanum],
                            verbose_name=_("Slug"),
                            help_text=_("Unique identifier for the shop used in the URL. "
                                        "It must contain only English letters, numerics, dashes (-), "
                                        "and underscores (_)"))

    email = models.EmailField(blank=True, null=True, verbose_name=_("Email"))
    contact_number = PhoneNumberField(blank=True, null=True, verbose_name=_("Contact Number"))
    image = ResizedImageField(null=True, size=[300, 300], quality=100, force_format=FORCED_IMAGE_FORMAT,
                              validators=[FileSizeValidator(max_upload_file_size=MAX_FILE_SIZE)],
                              upload_to='shops/', verbose_name=_("Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    order = models.PositiveIntegerField(default=0, blank=True, verbose_name=_('Order By'))

    # theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, related_name='shops',
    #                           verbose_name=_("Theme"))
    primary_color = models.CharField(max_length=7, null=True, validators=[validate_hex_color],
                                     verbose_name=_('Primary Color'),
                                     help_text=_("Primary color for template (e.g., #RRGGBB or #RGB)."))
    border_color = models.CharField(max_length=7, null=True, validators=[validate_hex_color],
                                     verbose_name=_('Border Color'),
                                     help_text=_("Border color for template (e.g., #RRGGBB or #RGB)."))

    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class HeaderImage(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="header_images",
                                   verbose_name=_("Header Image"))
    image = ResizedImageField(null=True, size=[1920, 1080], quality=100, force_format=FORCED_IMAGE_FORMAT,
                              validators=[FileSizeValidator(max_upload_file_size=MAX_FILE_SIZE)],
                              upload_to='headers/', verbose_name=_("Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"),
                                    help_text=_("Setting it to false, makes the image disappear from the page"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    class Meta:
        verbose_name = _('Home Page Image')
        verbose_name_plural = _('Home Page Images')
        ordering = ('-create_at', '-update_at')


class SocialMediaLink(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="social_media_links",
                                   verbose_name=_("Shop"))
    platform = models.CharField(max_length=20, choices=SocialMediaPlatform.choices, verbose_name=_("Platform"))
    url = models.CharField(max_length=250, null=True, verbose_name=_("Link / Phone Number"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _("Social Media Link")
        verbose_name_plural = _("Social Media Links")
        ordering = ('-create_at', '-update_at')


class Tag(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    icon = ResizedImageField(null=True, size=[300, 300], quality=100, force_format=FORCED_IMAGE_FORMAT,
                              validators=[FileSizeValidator(max_upload_file_size=MAX_FILE_SIZE)],
                              upload_to='tags/', verbose_name=_("Icon"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    order = models.PositiveIntegerField(default=0, blank=True, verbose_name=_('Order By'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ('order', '-create_at', '-update_at')

    def __str__(self):
        return self.name


class Travel(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="travels", verbose_name=_("Category"))

    name = models.CharField(max_length=255, verbose_name=_("Travel Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))

    origin_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="origin_travels",
                                       verbose_name=_("Origin Country"))
    origin_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="origin_travels",
                                    verbose_name=_("Origin City"))
    destination_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="destination_travels",
                                            verbose_name=_("Destination Country"))
    destination_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="destination_travels",
                                         verbose_name=_("Destination City"))

    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))

    duration = models.PositiveIntegerField(verbose_name=_("Duration (Days)"))

    image = ResizedImageField(null=True, size=[800, 500], quality=100, force_format=FORCED_IMAGE_FORMAT,
                              verbose_name=_("Image"))

    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Price"))
    after_sale_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True,
                                           verbose_name=_("Sale Price"))

    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.SET_NULL, related_name="travels",
                            verbose_name=_("Tag"))

    is_featured = models.BooleanField(default=False, verbose_name=_("Featured"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    order = models.PositiveIntegerField(default=0, blank=True, verbose_name=_('Order By'))

    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Create At"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Update At"))

    class Meta:
        verbose_name = _("Travel")
        verbose_name_plural = _("Travels")
        ordering = ('order', '-create_at', '-update_at')

    def __str__(self):
        return str(self.name)
