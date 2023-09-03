# Generated by Django 4.1 on 2023-09-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=30),
        ),
    ]
