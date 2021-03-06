# Generated by Django 3.0.1 on 2021-01-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_brand_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_side_banner',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='side_banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='brand',
            name='friendly_name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='has_logo',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='website',
            field=models.URLField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
