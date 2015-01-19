from modeltranslation.translator import translator, TranslationOptions
from category.models import Category_Instance
from category.models import Category_Content

class Category_InstanceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class Category_ContentTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category_Instance, Category_InstanceTranslationOptions)
translator.register(Category_Content, Category_ContentTranslationOptions)
