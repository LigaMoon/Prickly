# Generated by Django 3.1.5 on 2021-01-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210110_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True)),
        ),
    ]