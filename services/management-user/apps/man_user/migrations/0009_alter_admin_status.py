# Generated by Django 5.0.6 on 2024-05-24 03:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man_user', '0008_alter_kong_jwt_token_kong_jwt'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_status', to='master.status'),
        ),
    ]
