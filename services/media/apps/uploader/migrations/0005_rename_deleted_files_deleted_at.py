# Generated by Django 5.0.6 on 2024-06-19 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0004_files_filename_files_size_files_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='deleted',
            new_name='deleted_at',
        ),
    ]