# Generated by Django 3.1.5 on 2021-01-11 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210110_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='many_colors',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], help_text='Will the product come in multiple colors?', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='additional picture 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='additional picture 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='additional picture 4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateTimeField(help_text='Select today/now as the inout if the product is being published now.', verbose_name='product release date'),
        ),
    ]