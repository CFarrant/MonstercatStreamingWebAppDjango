# Generated by Django 3.0.3 on 2020-03-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200304_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album_name',
            field=models.CharField(db_column='album', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='track_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
