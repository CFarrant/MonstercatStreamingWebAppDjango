# Generated by Django 3.0.3 on 2020-03-04 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200304_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album',
            new_name='album_name',
        ),
    ]
