# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Instance',
            fields=[
                ('category_content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='category.Category_Content')),
                ('text', models.TextField()),
                ('text_de', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
            ],
            options={
            },
            bases=('category.category_content',),
        ),
    ]
