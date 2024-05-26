# Generated by Django 5.0.6 on 2024-05-26 06:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('mobile_phone', models.CharField(blank=True, max_length=25)),
                ('full_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_status', to='master.status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('mobile_phone', models.CharField(blank=True, max_length=25)),
                ('full_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer_status', to='master.status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Kong_JWT',
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
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Kong_JWT_Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('token', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
                ('kong_jwt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man_user.kong_jwt')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='kong_jwt',
            index=models.Index(fields=['kong_consumer_id'], name='man_user_ko_kong_co_7150b5_idx'),
        ),
        migrations.AddIndex(
            model_name='kong_jwt_token',
            index=models.Index(fields=['token'], name='man_user_ko_token_247411_idx'),
        ),
    ]
