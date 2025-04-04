from modeltranslation.translator import translator, TranslationOptions

from agency.models import Agency, Travel


class AgencyTranslationOptions(TranslationOptions):
    fields = ('name', )


class TravelTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(Agency, AgencyTranslationOptions)
translator.register(Travel, TravelTranslationOptions)
