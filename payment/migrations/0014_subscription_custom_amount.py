# Generated by Django 5.0.6 on 2025-02-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_alter_subscription_short_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='custom_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
