# Generated by Django 2.1.7 on 2019-04-02 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_auto_20190402_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subprogram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.SubProgram', verbose_name='Sub-Program'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, to='accounts.Teacher'),
        ),
        migrations.AlterField(
            model_name='program',
            name='coordinator',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Coordinator'),
        ),
        migrations.AlterField(
            model_name='subprogram',
            name='teachers',
            field=models.ManyToManyField(blank=True, to='accounts.Teacher'),
        ),
    ]
