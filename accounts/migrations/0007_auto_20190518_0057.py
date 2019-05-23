# Generated by Django 2.1.7 on 2019-05-18 00:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190518_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='auto_eval',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='Auto Evaluation'),
        ),
    ]
