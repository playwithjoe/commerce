# Generated by Django 4.0.6 on 2022-08-10 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0037_auction_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bid',
        ),
    ]
