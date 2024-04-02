from modeltranslation.translator import translator, TranslationOptions
from apps.product.models import ProductVariant, Product, Attribute, AttributeValue, Discount


class ProductTranslationOptions(TranslationOptions):
    fields = ["title"]


class ProductVariantTranslationOptions(TranslationOptions):
    fields = ["title", "description"]


class AttributeTranslationOptions(TranslationOptions):
    fields = ["title"]


class AttributeValueTranslationOptions(TranslationOptions):
    fields = ["value"]


class DiscountTranslationOptions(TranslationOptions):
    fields = ["name"]


translator.register(Product, ProductTranslationOptions)
translator.register(ProductVariant, ProductVariantTranslationOptions)
translator.register(Attribute, AttributeTranslationOptions)
translator.register(AttributeValue, AttributeValueTranslationOptions)
translator.register(Discount, DiscountTranslationOptions)