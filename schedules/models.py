from django.db import models
from multiselectfield import MultiSelectField


class Schedule(models.Model):
    TIME_CHOICES = (
        ('6', ''),
        ('7', ''),
        ('8', ''),
        ('9', ''),
        ('10', ''),
        ('11', ''),
        ('12', ''),
        ('13', ''),
        ('14', ''),
        ('15', ''),
        ('16', ''),
        ('17', ''),
        ('18', ''),
        ('19', ''),
        ('20', '')
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
