# Generated by Django 5.0.6 on 2024-05-19 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_title_task_task_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_title',
            new_name='title',
        ),
    ]
