# Generated by Django 4.0.6 on 2022-08-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_rename_title_auction_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bid',
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]
