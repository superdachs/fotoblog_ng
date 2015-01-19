from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

##
# Category instance class for managing the pages of the blog
##
@python_2_unicode_compatible
class Category_Instance(models.Model):

  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)

  def __str__(self):

    return self.title


##
# Content mapper class
#
@python_2_unicode_compatible
class Category_Content(models.Model):

  title = models.CharField(max_length=200)
  category = models.ForeignKey(Category_Instance, related_name='+')
  date_published = models.DateTimeField()
  author = models.ForeignKey(User)

  def __str__(self):

    return self.title


