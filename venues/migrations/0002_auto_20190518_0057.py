# Generated by Django 2.1.7 on 2019-05-18 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
