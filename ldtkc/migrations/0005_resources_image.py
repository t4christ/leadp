# Generated by Django 2.0 on 2019-03-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0004_auto_20181009_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='image',
            field=models.FileField(blank=True, max_length=1000, upload_to='https://storage.googleapis.com/bezop-uploads/media/'),
        ),
    ]
