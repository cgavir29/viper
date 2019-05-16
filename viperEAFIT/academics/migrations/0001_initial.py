# Generated by Django 2.1.7 on 2019-05-15 21:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
        ('venues', '__first__'),
        ('schedules', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.CharField(choices=[('Intensivo', 'Intensivo'), ('Semi-Intensivo', 'Semi-Intensivo'), ('Regular', 'Regular')], max_length=15)),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='End Date (YYYY-MM-DD)')),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('coordinator', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Coordinator')),
            ],
        ),
        migrations.CreateModel(
            name='SubProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Program')),
                ('teachers', models.ManyToManyField(blank=True, to='accounts.Teacher')),
            ],
            options={
                'verbose_name': 'Sub-Program',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='subprogram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.SubProgram', verbose_name='Sub-Program'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='accounts.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='academics.Course'),
        ),
        migrations.AddField(
            model_name='class',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='schedules.Schedule'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='accounts.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='venues.Venue'),
        ),
        migrations.AlterUniqueTogether(
            name='subprogram',
            unique_together={('name', 'program')},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'subprogram')},
        ),
    ]
