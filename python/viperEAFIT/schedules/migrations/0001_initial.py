# Generated by Django 2.1.7 on 2019-04-02 02:09

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
                ('intensity', models.CharField(choices=[('IN', 'Intensivo'), ('SI', 'Semi-Intensivo'), ('RE', 'Regular')], max_length=15)),
                ('monday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6to7', '6:00 - 7:00'), ('7to8', '7:00 - 8:00'), ('8to9', '8:00 - 9:00'), ('9to10', '9:00 - 10:00'), ('10to11', '10:00 - 11:00'), ('11to12', '11:00 - 12:00'), ('12to13', '12:00 - 13:00'), ('13to14', '13:00 - 14:00'), ('14to15', '14:00 - 15:00'), ('15to16', '15:00 - 16:00'), ('16to17', '16:00 - 17:00'), ('17to18', '17:00 - 18:00'), ('18to19', '18:00 - 19:00'), ('19to20', '19:00 - 20:00'), ('20to21', '20:00 - 21:00')], max_length=97, null=True)),
                ('tuesday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6to7', '6:00 - 7:00'), ('7to8', '7:00 - 8:00'), ('8to9', '8:00 - 9:00'), ('9to10', '9:00 - 10:00'), ('10to11', '10:00 - 11:00'), ('11to12', '11:00 - 12:00'), ('12to13', '12:00 - 13:00'), ('13to14', '13:00 - 14:00'), ('14to15', '14:00 - 15:00'), ('15to16', '15:00 - 16:00'), ('16to17', '16:00 - 17:00'), ('17to18', '17:00 - 18:00'), ('18to19', '18:00 - 19:00'), ('19to20', '19:00 - 20:00'), ('20to21', '20:00 - 21:00')], max_length=97, null=True)),
                ('wednesday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6to7', '6:00 - 7:00'), ('7to8', '7:00 - 8:00'), ('8to9', '8:00 - 9:00'), ('9to10', '9:00 - 10:00'), ('10to11', '10:00 - 11:00'), ('11to12', '11:00 - 12:00'), ('12to13', '12:00 - 13:00'), ('13to14', '13:00 - 14:00'), ('14to15', '14:00 - 15:00'), ('15to16', '15:00 - 16:00'), ('16to17', '16:00 - 17:00'), ('17to18', '17:00 - 18:00'), ('18to19', '18:00 - 19:00'), ('19to20', '19:00 - 20:00'), ('20to21', '20:00 - 21:00')], max_length=97, null=True)),
                ('thursday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6to7', '6:00 - 7:00'), ('7to8', '7:00 - 8:00'), ('8to9', '8:00 - 9:00'), ('9to10', '9:00 - 10:00'), ('10to11', '10:00 - 11:00'), ('11to12', '11:00 - 12:00'), ('12to13', '12:00 - 13:00'), ('13to14', '13:00 - 14:00'), ('14to15', '14:00 - 15:00'), ('15to16', '15:00 - 16:00'), ('16to17', '16:00 - 17:00'), ('17to18', '17:00 - 18:00'), ('18to19', '18:00 - 19:00'), ('19to20', '19:00 - 20:00'), ('20to21', '20:00 - 21:00')], max_length=97, null=True)),
                ('friday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6to7', '6:00 - 7:00'), ('7to8', '7:00 - 8:00'), ('8to9', '8:00 - 9:00'), ('9to10', '9:00 - 10:00'), ('10to11', '10:00 - 11:00'), ('11to12', '11:00 - 12:00'), ('12to13', '12:00 - 13:00'), ('13to14', '13:00 - 14:00'), ('14to15', '14:00 - 15:00'), ('15to16', '15:00 - 16:00'), ('16to17', '16:00 - 17:00'), ('17to18', '17:00 - 18:00'), ('18to19', '18:00 - 19:00'), ('19to20', '19:00 - 20:00'), ('20to21', '20:00 - 21:00')], max_length=97, null=True)),
                ('saturday', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('6to7', '6:00 - 7:00'), ('7to8', '7:00 - 8:00'), ('8to9', '8:00 - 9:00'), ('9to10', '9:00 - 10:00'), ('10to11', '10:00 - 11:00'), ('11to12', '11:00 - 12:00'), ('12to13', '12:00 - 13:00'), ('13to14', '13:00 - 14:00'), ('14to15', '14:00 - 15:00'), ('15to16', '15:00 - 16:00'), ('16to17', '16:00 - 17:00'), ('17to18', '17:00 - 18:00'), ('18to19', '18:00 - 19:00'), ('19to20', '19:00 - 20:00'), ('20to21', '20:00 - 21:00')], max_length=97, null=True)),
            ],
        ),
    ]