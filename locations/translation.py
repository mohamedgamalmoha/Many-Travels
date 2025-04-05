from modeltranslation.translator import translator, TranslationOptions

from locations.models import Country, City, State


class NameTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Country,  NameTranslationOptions)
translator.register(City, NameTranslationOptions)
translator.register(State, NameTranslationOptions)
