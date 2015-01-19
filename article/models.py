from __future__ import unicode_literals
from django.db import models
from category.models import Category_Content
from django.utils.encoding import python_2_unicode_compatible

##
# Instance class for managing articles
##
@python_2_unicode_compatible
class Article_Instance(Category_Content):

  text = models.TextField()

  def __str__(self):

    return "%s" % (self.title)

