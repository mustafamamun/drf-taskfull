# Generated by Django 3.2.6 on 2021-11-03 20:31

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=users.models.GenerateProfileImagePath()),
        ),
    ]
