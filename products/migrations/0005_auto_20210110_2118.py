# Generated by Django 3.1.5 on 2021-01-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210110_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avg_rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2, null=True, verbose_name='average product rating'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_pic',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='thumbnail picture'),
        ),
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateTimeField(verbose_name='product release date'),
        ),
    ]