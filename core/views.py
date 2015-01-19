from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from category.models import Category_Instance
from article.models import Article_Instance
from gallery.models import Gallery_Instance, Gallery_Image
from operator import itemgetter

def page(request, name, content_categories):

  categories = Category_Instance.objects.all()

  if content_categories is None:
    content_categories = categories

  content_entries = []

  for content_category in content_categories:
    for content_entry in Article_Instance.objects.filter(category__exact=content_category):
      content_entries.append(content_entry)
    for content_entry in Gallery_Instance.objects.filter(category__exact=content_category):
      gallery_images = []
      for gallery_image in Gallery_Image.objects.filter(gallery__exact=content_entry):
        gallery_images.append(gallery_image)
      content_entry.images = gallery_images
      content_entries.append(content_entry)

    for pos_upper in xrange(len(content_entries)-1,0,-1):
      for i in xrange(pos_upper):
        if content_entries[i].date_published < content_entries[i+1].date_published:
          content_entries[i], content_entries[i+1] = content_entries[i+1], content_entries[i]


  context = {'name': name,
      'categories': categories,
      'content_entries': content_entries,
    }

  return render(request, 'core/page.phtml', context)

##
# Definition of the index view
##
def index(request):

  return page(request, 'home', None)

##
# Definition of the site view
## 
def site(request, category):


  print(category)
  category_instance = Category_Instance.objects.filter(title__exact=category)

  return page(request, category_instance, category_instance)
