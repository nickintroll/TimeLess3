# Generated by Django 4.1 on 2023-09-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_remove_order_contacts_order_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('special', '-order', 'created')},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('is_primary',)},
        ),
        migrations.CreateModel(
            name='ProductParamater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('value', models.CharField(max_length=120)),
                ('product', models.ManyToManyField(related_name='parameters', to='shop.product')),
            ],
        ),
    ]
