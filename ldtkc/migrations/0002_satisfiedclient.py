# Generated by Django 2.0 on 2018-06-08 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ldtkc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatisfiedClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='https://storage.googleapis.com/bezop-uploads/media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ldtkc_satisfied', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]