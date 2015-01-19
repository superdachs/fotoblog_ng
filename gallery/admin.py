from django.contrib import admin
from gallery.models import Gallery_Instance
from gallery.models import Gallery_Image


class ImagesInline(admin.StackedInline):
    model = Gallery_Image
    extra = 1
    readonly_fields = [
        'image_tag',
    ]

class Gallery_InstanceAdmin(admin.ModelAdmin):

    inlines = [
        ImagesInline,
    ]

admin.site.register(Gallery_Instance, Gallery_InstanceAdmin)


#https://code.djangoproject.com/wiki/CookBookNewformsAdminAndUser
