# Generated by Django 5.0.6 on 2024-12-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_userprofile_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]