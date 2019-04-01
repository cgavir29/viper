# Generated by Django 2.1.7 on 2019-03-27 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20190321_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Course'),
        ),
        migrations.AlterField(
            model_name='class',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.Venue'),
        ),
    ]
