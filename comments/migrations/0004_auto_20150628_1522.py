# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20150621_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='children',
            field=models.ManyToManyField(related_name='children_rel_+', to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
