# Generated by Django 5.0.6 on 2024-08-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_alter_payment_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]