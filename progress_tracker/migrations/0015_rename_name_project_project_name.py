# Generated by Django 5.0.6 on 2024-08-29 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracker', '0014_progress_role_alter_progress_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_name',
        ),
    ]