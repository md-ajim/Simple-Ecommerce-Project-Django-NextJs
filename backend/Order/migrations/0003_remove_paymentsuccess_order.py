# Generated by Django 5.1 on 2024-11-26 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_paymentsuccess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentsuccess',
            name='order',
        ),
    ]
