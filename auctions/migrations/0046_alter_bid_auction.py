# Generated by Django 4.0.6 on 2022-09-06 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_rename_listing_bid_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='auction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listing'),
        ),
    ]
