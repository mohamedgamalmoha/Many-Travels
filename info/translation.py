from modeltranslation.translator import translator, TranslationOptions

from info.models import MainInfo, Service, AboutUs, Theme


class TitleWithDescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(MainInfo, TitleWithDescriptionTranslationOptions)
translator.register(Service, TitleWithDescriptionTranslationOptions)
translator.register(AboutUs, TitleWithDescriptionTranslationOptions)
translator.register(Theme, TitleWithDescriptionTranslationOptions)
