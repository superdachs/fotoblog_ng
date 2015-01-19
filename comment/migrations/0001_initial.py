# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('show_email', models.BooleanField(default=False)),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('entry', models.ForeignKey(to='category.Category_Content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
