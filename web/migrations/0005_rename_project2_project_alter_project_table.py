# Generated by Django 4.2.5 on 2023-09-20 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_project2_surveyresponses_delete_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project2',
            new_name='Project',
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
    ]