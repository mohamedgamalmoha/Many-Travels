from django.db import models
from django.utils.translation import gettext_lazy as _


class SocialMediaPlatform(models.TextChoices):
    FACEBOOK = 'facebook', _("Facebook")
    TWITTER = 'twitter', _("Twitter")
    INSTAGRAM = 'instagram', _("Instagram")
    TIKTOK = 'tiktok', _("TikTok")
    YOUTUBE = 'youtube', _("YouTube")
    PINTEREST = 'pinterest', _("Pinterest")
    PHONE_NUMBER_1 = 'phone_number_1', _('Phone Number 1')
    PHONE_NUMBER_2 = 'phone_number_2', _('Phone Number 2')


class DaysOfWeekChoice(models.TextChoices):
    SATURDAY = 'SAT', _("Saturday")
    SUNDAY = 'SUN', _("Sunday")
    MONDAY = 'MON', _("Monday")
    TUESDAY = 'TUE', _("Tuesday")
    WEDNESDAY = 'WED', _("Wednesday")
    THURSDAY = 'THU', _("Thursday")
    FRIDAY = 'FRI', _("Friday")


class TravelType(models.TextChoices):
    SINGLE = 'single', _("Single")
    COUPLE = 'couple', _("Couple")
    FAMILY = 'family', _("Family")
    GROUP = 'group', _("Group")


class HousingType(models.TextChoices):
    APARTMENT = 'apartment', _("Apartment")
    VILLA = 'villa', _("Villa")
    HOSTEL = 'hostel', _("Hostel")
    CAMPING = 'camping', _("Camping")
    GUESTHOUSE = 'guesthouse', _("Guesthouse")
    RESORT = 'resort', _("Resort")
    ONE_STAR_HOTEL = '1_star_hotel', _("1 Star Hotel")
    TWO_STAR_HOTEL = '2_star_hotel', _("2 Star Hotel")
    THREE_STAR_HOTEL = '3_star_hotel', _("3 Star Hotel")
    FOUR_STAR_HOTEL = '4_star_hotel', _("4 Star Hotel")
    FIVE_STAR_HOTEL = '5_star_hotel', _("5 Star Hotel")
