# Generated by Django 2.1.7 on 2019-05-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190516_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='epik_unique_number',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Epik Unique Number'),
        ),
    ]
