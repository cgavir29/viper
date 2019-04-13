from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Schedule(models.Model):
    TIME_CHOICES = (
        ('6to7', '6:00 - 7:00'),
        ('7to8', '7:00 - 8:00'),
        ('8to9', '8:00 - 9:00'),
        ('9to10', '9:00 - 10:00'),
        ('10to11', '10:00 - 11:00'),
        ('11to12', '11:00 - 12:00'),
        ('12to13', '12:00 - 13:00'),
        ('13to14', '13:00 - 14:00'),
        ('14to15', '14:00 - 15:00'),
        ('15to16', '15:00 - 16:00'),
        ('16to17', '16:00 - 17:00'),
        ('17to18', '17:00 - 18:00'),
        ('18to19', '18:00 - 19:00'),
        ('19to20', '19:00 - 20:00'),
        ('20to21', '20:00 - 21:00')
    )

    SEMESTRAL = 'SM'
    REGULAR = 'RE'
    SEMI_INTENSIVO = 'SI'
    INTENSIVO = 'IN'
    ULTRA = 'UL'

    INTENSITY_CHOICES = (
        # (ULTRA, 'Ultra'),
        (INTENSIVO, 'Intensivo'),
        # (SEMESTRAL, 'Semestral'),
        (SEMI_INTENSIVO, 'Semi-Intensivo'),
        (REGULAR, 'Regular'),
    )

    name = models.CharField(max_length=100, unique=True)
    intensity = models.CharField(max_length=15, choices=INTENSITY_CHOICES)
    monday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    tuesday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    wednesday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    thursday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    friday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    saturday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
