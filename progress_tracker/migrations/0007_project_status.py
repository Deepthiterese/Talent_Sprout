# Generated by Django 5.0.6 on 2024-07-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracker', '0006_remove_project_slug_alter_progress_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('terminated', 'Terminated')], default='active', max_length=20),
        ),
    ]