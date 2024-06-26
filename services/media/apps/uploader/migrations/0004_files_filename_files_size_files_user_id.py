# Generated by Django 5.0.6 on 2024-06-19 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_files_path_files_type_files_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='filename',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='files',
            name='size',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='files',
            name='user_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
