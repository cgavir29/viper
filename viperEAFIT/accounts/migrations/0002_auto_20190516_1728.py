# Generated by Django 2.1.7 on 2019-05-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='identification',
        ),
        migrations.AlterField(
            model_name='user',
            name='epik_unique_number',
            field=models.IntegerField(blank=True, verbose_name='Epik Unique Number'),
        ),
    ]