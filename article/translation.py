from modeltranslation.translator import translator, TranslationOptions
from article.models import Article_Instance

class Article_InstanceTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Article_Instance, Article_InstanceTranslationOptions)
