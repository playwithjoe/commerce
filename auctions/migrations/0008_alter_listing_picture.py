# Generated by Django 3.2.9 on 2022-04-23 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_listing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
