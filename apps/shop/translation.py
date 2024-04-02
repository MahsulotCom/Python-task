from modeltranslation.translator import translator, TranslationOptions
from apps.shop.models import Shop


class ShopTranslationOptions(TranslationOptions):
    fields = ["title", "description"]

translator.register(Shop, ShopTranslationOptions)