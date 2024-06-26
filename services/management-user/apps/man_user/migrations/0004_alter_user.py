# Generated by Django 5.0.6 on 2024-05-18 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('man_user', '0001_initial'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE auth_user MODIFY COLUMN first_name varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL"),
        migrations.RunSQL("ALTER TABLE auth_user MODIFY COLUMN last_name varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL"),
        migrations.RunSQL("CREATE UNIQUE INDEX auth_user_email_IDX2 USING BTREE ON auth_user (email)"),
    ]
