from django.db import models
from multiselectfield import MultiSelectField


class Schedule(models.Model):
    TIME_CHOICES = (
        ('6to7', ''),
        ('7to8', ''),
        ('8to9', ''),
        ('9to10', ''),
        ('10to11', ''),
        ('11to12', ''),
        ('12to13', ''),
        ('13to14', ''),
        ('14to15', ''),
        ('15to16', ''),
        ('16to17', ''),
        ('17to18', ''),
        ('18to19', ''),
        ('19to20', ''),
        ('20to21', '')
    )

    INTENSIVO = 'Intensivo'
    SEMI_INTENSIVO = 'Semi-Intensivo'
    REGULAR = 'Regular'
    INTENSITY_CHOICES = (
        (INTENSIVO, INTENSIVO),
        (SEMI_INTENSIVO, SEMI_INTENSIVO),
        (REGULAR, REGULAR), 
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
