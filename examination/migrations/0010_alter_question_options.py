# Generated by Django 5.0.6 on 2025-01-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0009_remove_question_code_editor_placeholder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.JSONField(default=list),
        ),
    ]
