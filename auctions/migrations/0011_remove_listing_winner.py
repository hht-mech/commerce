# Generated by Django 3.0.8 on 2020-07-14 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listing_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='winner',
        ),
    ]
