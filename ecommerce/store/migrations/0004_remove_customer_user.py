# Generated by Django 5.0.6 on 2024-06-28 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]