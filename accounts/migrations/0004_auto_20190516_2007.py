# Generated by Django 2.1.7 on 2019-05-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190516_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='epik_unique_number',
            field=models.IntegerField(unique=True, verbose_name='Epik Unique Number'),
        ),
    ]
