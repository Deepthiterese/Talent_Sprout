# Generated by Django 5.0.6 on 2024-10-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0005_alter_question_correct_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]