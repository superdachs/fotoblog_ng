# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('date_published', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category_Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('description_de', models.TextField(null=True, blank=True)),
                ('description_en', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category_content',
            name='category',
            field=models.ForeignKey(related_name='+', to='category.Category_Instance'),
            preserve_default=True,
        ),
    ]
