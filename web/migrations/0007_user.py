# Generated by Django 4.2.5 on 2023-10-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_rename_project_id_surveyresponses_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
    ]
