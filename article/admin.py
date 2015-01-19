from django.contrib import admin
from article.models import Article_Instance
from modeltranslation.admin import TranslationAdmin
#from django_summernote.admin import SummernoteModelAdmin

class Article_InstanceAdmin(TranslationAdmin):
  pass


admin.site.register(Article_Instance, Article_InstanceAdmin)

