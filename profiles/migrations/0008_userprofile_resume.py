# Generated by Django 5.0.6 on 2024-07-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_projectexperience_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]