# Generated by Django 4.2.5 on 2023-10-12 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]