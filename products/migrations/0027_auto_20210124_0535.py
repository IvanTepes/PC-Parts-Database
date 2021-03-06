# Generated by Django 3.0.1 on 2021-01-24 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
        ('products', '0026_auto_20210124_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='additional_ogo',
        ),
        migrations.AddField(
            model_name='product',
            name='additional_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='additional_logos', to='setup.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True),
        ),
    ]
