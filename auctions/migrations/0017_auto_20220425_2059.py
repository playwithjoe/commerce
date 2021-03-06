# Generated by Django 3.2.9 on 2022-04-26 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_rename_listing_watchlist_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='favorite',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
