# Generated by Django 3.1.5 on 2021-01-20 23:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20210120_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Enter phone number in a format: '+111111111' and no longer that 15 digits.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]