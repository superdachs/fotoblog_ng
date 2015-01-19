# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='default.png', upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gallery_Instance',
            fields=[
                ('category_content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='category.Category_Content')),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=('category.category_content',),
        ),
        migrations.AddField(
            model_name='gallery_image',
            name='gallery',
            field=models.ForeignKey(to='gallery.Gallery_Instance'),
            preserve_default=True,
        ),
    ]
