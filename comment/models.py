from django.db import models
from category.models import Category_Content

class comment(models.Model):

  author = models.CharField(max_length=40)
  email = models.EmailField(max_length=254)
  show_email = models.BooleanField(default=False)
  text = models.TextField(max_length=1000)
  date = models.DateTimeField(auto_now=True, auto_now_add=True)
  entry = models.ForeignKey(Category_Content)

