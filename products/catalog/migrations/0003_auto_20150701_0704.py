# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(null=True, upload_to=b'images/product_image', blank=True),
        ),
    ]
