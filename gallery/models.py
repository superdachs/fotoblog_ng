from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from category.models import Category_Content
from fotoblog_ng import settings

##
# Instance class for managing galleries
##
@python_2_unicode_compatible
class Gallery_Instance(Category_Content):

  description = models.TextField(blank=True)

  def __str__(self):

    return self.title

##
# Image class for holding gallery images
##
@python_2_unicode_compatible
class Gallery_Image(models.Model):

  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  gallery = models.ForeignKey(Gallery_Instance)
  image = models.ImageField(default='default.png')

  def image_tag(self):
    print(self.image)
    print(self.image.url)
    return '<img style="max-width: 100px; max-height: 100px;" src="%s" />' % self.image.url

  image_tag.short_description = 'Preview'
  image_tag.allow_tags = True

  def __str__(self):

    return self.title

