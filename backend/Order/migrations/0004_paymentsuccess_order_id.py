# Generated by Django 5.1 on 2024-11-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_remove_paymentsuccess_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsuccess',
            name='order_id',
            field=models.CharField(default='ABC1926', max_length=20),
        ),
    ]
