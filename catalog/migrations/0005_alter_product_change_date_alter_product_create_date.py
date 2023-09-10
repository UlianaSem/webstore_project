# Generated by Django 4.2.4 on 2023-09-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='change_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='дата создания'),
        ),
    ]