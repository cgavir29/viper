# Generated by Django 2.1.7 on 2019-04-02 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subprogram',
            options={'verbose_name': 'Sub-Program'},
        ),
        migrations.AlterField(
            model_name='program',
            name='coordinator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Coordinator'),
        ),
    ]