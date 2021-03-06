# Generated by Django 4.0.3 on 2022-04-02 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Profesion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='profile',
            name='local_govt',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(blank=True, max_length=55),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
