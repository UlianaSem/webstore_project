# Generated by Django 4.2.4 on 2023-08-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, verbose_name='адрес')),
                ('telephone_number', models.CharField(max_length=50, verbose_name='номер телефона')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
            ],
            options={
                'verbose_name': 'контактные данные',
                'verbose_name_plural': 'контактные данные',
            },
        ),
    ]
