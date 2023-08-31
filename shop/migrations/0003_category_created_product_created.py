# Generated by Django 4.1 on 2023-08-31 11:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 8, 31, 11, 56, 43, 812592, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]