# Generated by Django 5.0.6 on 2024-06-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='files',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]