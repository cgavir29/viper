# Generated by Django 2.1.7 on 2019-03-20 19:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0001_initial'),
        ('venues', '0001_initial'),
        ('schedules', '0001_initial'),
        ('accounts', '0006_auto_20190320_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.CharField(choices=[('SM', 'Semestral'), ('RE', 'Regular'), ('SI', 'Semi-Intensivo'), ('IN', 'Intensivo'), ('UL', 'Ultra')], default='RE', max_length=15)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='academics.Course')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.Schedule')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Teacher')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='venues.Venue')),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
    ]
