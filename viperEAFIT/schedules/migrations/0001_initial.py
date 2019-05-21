# Generated by Django 2.1.7 on 2019-05-16 17:16

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('intensity', models.CharField(choices=[('Intensivo', 'Intensivo'), ('Semi-Intensivo', 'Semi-Intensivo'), ('Regular', 'Regular')], max_length=15)),
                ('monday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6', '6:00 - 7:00'), ('7', '7:00 - 8:00'), ('8', '8:00 - 9:00'), ('9', '9:00 - 10:00'), ('10', '10:00 - 11:00'), ('11', '11:00 - 12:00'), ('12', '12:00 - 13:00'), ('13', '13:00 - 14:00'), ('14', '14:00 - 15:00'), ('15', '15:00 - 16:00'), ('16', '16:00 - 17:00'), ('17', '17:00 - 18:00'), ('18', '18:00 - 19:00'), ('19', '19:00 - 20:00'), ('20', '20:00 - 21:00')], max_length=40, null=True)),
                ('tuesday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6', '6:00 - 7:00'), ('7', '7:00 - 8:00'), ('8', '8:00 - 9:00'), ('9', '9:00 - 10:00'), ('10', '10:00 - 11:00'), ('11', '11:00 - 12:00'), ('12', '12:00 - 13:00'), ('13', '13:00 - 14:00'), ('14', '14:00 - 15:00'), ('15', '15:00 - 16:00'), ('16', '16:00 - 17:00'), ('17', '17:00 - 18:00'), ('18', '18:00 - 19:00'), ('19', '19:00 - 20:00'), ('20', '20:00 - 21:00')], max_length=40, null=True)),
                ('wednesday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6', '6:00 - 7:00'), ('7', '7:00 - 8:00'), ('8', '8:00 - 9:00'), ('9', '9:00 - 10:00'), ('10', '10:00 - 11:00'), ('11', '11:00 - 12:00'), ('12', '12:00 - 13:00'), ('13', '13:00 - 14:00'), ('14', '14:00 - 15:00'), ('15', '15:00 - 16:00'), ('16', '16:00 - 17:00'), ('17', '17:00 - 18:00'), ('18', '18:00 - 19:00'), ('19', '19:00 - 20:00'), ('20', '20:00 - 21:00')], max_length=40, null=True)),
                ('thursday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6', '6:00 - 7:00'), ('7', '7:00 - 8:00'), ('8', '8:00 - 9:00'), ('9', '9:00 - 10:00'), ('10', '10:00 - 11:00'), ('11', '11:00 - 12:00'), ('12', '12:00 - 13:00'), ('13', '13:00 - 14:00'), ('14', '14:00 - 15:00'), ('15', '15:00 - 16:00'), ('16', '16:00 - 17:00'), ('17', '17:00 - 18:00'), ('18', '18:00 - 19:00'), ('19', '19:00 - 20:00'), ('20', '20:00 - 21:00')], max_length=40, null=True)),
                ('friday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6', '6:00 - 7:00'), ('7', '7:00 - 8:00'), ('8', '8:00 - 9:00'), ('9', '9:00 - 10:00'), ('10', '10:00 - 11:00'), ('11', '11:00 - 12:00'), ('12', '12:00 - 13:00'), ('13', '13:00 - 14:00'), ('14', '14:00 - 15:00'), ('15', '15:00 - 16:00'), ('16', '16:00 - 17:00'), ('17', '17:00 - 18:00'), ('18', '18:00 - 19:00'), ('19', '19:00 - 20:00'), ('20', '20:00 - 21:00')], max_length=40, null=True)),
                ('saturday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6', '6:00 - 7:00'), ('7', '7:00 - 8:00'), ('8', '8:00 - 9:00'), ('9', '9:00 - 10:00'), ('10', '10:00 - 11:00'), ('11', '11:00 - 12:00'), ('12', '12:00 - 13:00'), ('13', '13:00 - 14:00'), ('14', '14:00 - 15:00'), ('15', '15:00 - 16:00'), ('16', '16:00 - 17:00'), ('17', '17:00 - 18:00'), ('18', '18:00 - 19:00'), ('19', '19:00 - 20:00'), ('20', '20:00 - 21:00')], max_length=40, null=True)),
            ],
        ),
    ]
