# Generated by Django 5.0.6 on 2024-05-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man_user', '0005_remove_kong_jwt_deleted_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kong_jwt',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='kong_jwt',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]