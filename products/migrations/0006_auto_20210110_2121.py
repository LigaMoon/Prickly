# Generated by Django 3.1.5 on 2021-01-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210110_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateTimeField(help_text='Select today/now as the input if the product is being published now.', verbose_name='product release date'),
        ),
    ]