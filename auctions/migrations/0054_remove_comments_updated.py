# Generated by Django 4.0.4 on 2022-09-15 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0053_comments_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='updated',
        ),
    ]
