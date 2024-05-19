# Generated by Django 5.0.6 on 2024-05-19 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man_user', '0002_auto_20240518_1811'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KongJWT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('jwt_id', models.CharField(blank=True, max_length=255, null=True)),
                ('jwt_key', models.CharField(blank=True, max_length=255, null=True)),
                ('jwt_secret', models.CharField(max_length=255, null=True)),
                ('rsa_public_key', models.TextField(null=True)),
                ('kong_consumer_id', models.CharField(max_length=255, null=True)),
                ('algorithm', models.CharField(max_length=50, null=True)),
                ('request_body', models.JSONField(null=True)),
                ('response_body', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]