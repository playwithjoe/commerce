# Generated by Django 4.0.6 on 2022-08-18 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_bid_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
